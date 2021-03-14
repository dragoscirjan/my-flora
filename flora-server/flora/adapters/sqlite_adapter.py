import sqlite3
from flora.models import HistoryItem

class SqliteAdapter(object):

  def __init__(self, **kwargs):
    if not 'database' in kwargs:
      raise ErrorError('Please configure database path.')
    self.database = kwargs.get('database')


  def add_history_item(self, item: HistoryItem) -> None:
    with sqlite3.connect('example.db') as conn:
      query = '''
INSERT INTO "history_items" (
  "plant_tag",
  "device_time",
  "wall_time",
  "temperature",
  "light",
  "moisture",
  "conductivity",
  "batery_level",
  "firmware_version"
) VALUES (
  "{plant_tag}",
  "{device_time}",
  "{wall_time}",
  "{temperature}",
  "{light}",
  "{moisture}",
  "{conductivity}",
  "{batery_level}",
  "{firmware_version}"
)
'''.format(item.__dict__)
      print(query)
      # conn.execute(query)
