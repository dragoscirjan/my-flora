from config2.config import config as file_config
from dependency_injector import containers, providers
from flora.db import Base as DbBase, Sqlite
from flora.controllers import DevicesController
from flora.routes import RouteDispatcher
from typing import Type

file_config.get()

def db_adapter_callable(adapter: Type[DbBase] = None, config: dict = {}) -> DbBase:
  print('adapter: ', adapter)
  print('config: ', config)
  return adapter(**config)

class Container(containers.DeclarativeContainer):

  config = providers.Configuration()

  db_sqlite_adapter = providers.Factory(
    Sqlite,
  )
  db_sqlite_adapter.add_kwargs(config=config.db.config)

  db_adapter = providers.Selector(
    config.sqlite_or_none,
    sqlite=db_sqlite_adapter,
    none=providers.Factory(DbBase)
  )

  devices_controller = providers.Singleton(
    DevicesController,
    db_adapter=db_adapter
  )

  route_dispatcher = providers.Singleton(
    RouteDispatcher,
    DevicesController=devices_controller
  )


db_config = file_config.db

container = Container()
container.config.from_dict({
  'sqlite_or_none': db_config.adapter,
  'db': {
    'config': {
      'database': 'my_flora.sqlite'
    } if not db_config or not db_config.config else db_config.config
  }
})
