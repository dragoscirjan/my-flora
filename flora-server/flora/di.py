from config2.config import config as file_config
from dependency_injector import containers, providers
from btlewrap import bluepy, pygatt
from miflora.miflora_poller import MiFloraPoller
from flora.db import Sqlite
from flora.controllers import DevicesController
from flora.mi import DevicePollerWrapper
from flora.routes import RouteDispatcher

file_config.get()

class DevicePollerAdapters:
  bluepy = 'bluepy'
  pygatt = 'pygatt'

def device_poller_backend(adapter: str):
  return bluepy.BluepyBackend if adapter == DevicePollerAdapters.bluepy else \
          pygatt.PygattBackend if adapter == DevicePollerAdapters.pygatt else None

def db_adapter(adapter: str):
  return

class Container(containers.DeclarativeContainer):

  config = providers.Configuration()

  miflora_device_poller = providers.Factory(
    MiFloraPoller,
    backend=config.miflora.poller.adapter
  )

  device_poller_wrapper = providers.Factory(
    DevicePollerWrapper,
    poller=miflora_device_poller
  )

  db_adapter = providers.Singleton(
    config.db.adapter,
    config=config.db.config,
  )

  devices_controller = providers.Singleton(
    DevicesController,
    db_adapter=db_adapter
  )

  route_dispatcher = providers.Singleton(
    RouteDispatcher,
    controllers={
      'DevicesController': devices_controller
    }
  )


db_config = file_config.db
bt_adapter = file_config.miflora.poller.adapter

container = Container()
container.config.from_dict({
  'db': {
    'adapter': Sqlite if not db_config or not db_config.adapter or db_config.adapter == 'sqlite' else None,
    'config': {
      'database': 'my_flora.sqlite'
    } if not db_config or not db_config.config else db_config.config
  },
  'miflora': {
    'poller': {
      'adapter': bluepy.BluepyBackend if not bt_adapter or bt_adapter.lower() == 'bluepy'\
                  else pygatt.PygattBackend if bt_adapter.lower() == 'pygatt' else None
    }
  }
})
