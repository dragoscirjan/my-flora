from config2.config import config
from flora.adapters.sqlite_adapter import SqliteAdapter

class DB:
  def get_adapter():
    if config.db is None:
      raise Exception('No database config')
    if config.db.adapter is None:
      raise Exception('No database adapter defined')
    if config.db.adapter == 'sqlite':
      return SqliteAdapter(**config.adapter.config)
    raise Exception('No known adapter defined. Please use: sqlite')
