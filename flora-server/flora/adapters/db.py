from config2.config import config
from flora.adapters.sqlite_adapter import SqliteAdapter

db_adapter = None

class DB:
  def get_adapter():
    if db_adapter is None:
      if config.db is None:
        raise Exception('No database config')
      if config.db.adapter is None:
        raise Exception('No database adapter defined')
      if config.db.adapter == 'sqlite':
        db_adapter = SqliteAdapter(**config.adapter.config)
      else:
        raise Exception('No known adapter defined. Please use: sqlite')
    return db_adapter
