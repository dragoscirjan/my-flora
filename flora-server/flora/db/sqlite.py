import sqlite3
from flora.db import Base
from flora.models import HistoryItem


class Sqlite(Base):

  def __init__(self, config: dict = {}):
    self._conn = sqlite3.connect(**config)

  def add_history_item(self, item: HistoryItem) -> None:
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
