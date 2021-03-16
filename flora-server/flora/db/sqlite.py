import sqlite3
from flora.db import Base
from flora.models import HistoryItem


class Sqlite(Base):

  def __init__(self, config: dict = {}):
    self._config = config
    # self._conn = sqlite3.connect(**config)

  def add_history_item(self, item: HistoryItem = None) -> None:
    query = '''
INSERT INTO "history_items" (
  "address",
  "plant_tag",
  "device_time",
  "temperature",
  "light",
  "moisture",
  "conductivity",
  "batery_level",
  "firmware_version"
) VALUES (
  "{address}",
  "{plant_tag}",
  "{device_time}",
  "{temperature}",
  "{light}",
  "{moisture}",
  "{conductivity}",
  "{batery_level}",
  "{firmware_version}"
)
'''.format(**item)

    cursor = sqlite3.connect(**self._config).cursor()
    cursor.execute()
    cursor.close()

  def get_latest_history_item(self, address: str) -> HistoryItem:
    query = '''
  SELECT * FROM history_items hi WHERE hi.address = '{address}' ORDER BY hi.device_time DESC LIMIT 0, 1
'''.format(address=address)

    cursor = sqlite3.connect(**self._config).cursor()
    cursor.execute(query)
    (id,
     address,
     plant_tag,
     device_time,
     temperature,
     light,
     moisture,
     conductivity,
     batery_level,
     firmware_version) = cursor.fetchone()
    cursor.close()

    return HistoryItem(
      address=address,
      plant_tag=plant_tag,
      device_time=device_time,
      temperature=temperature,
      light=light,
      moisture=moisture,
      conductivity=conductivity,
      batery_level=batery_level,
      firmware_version=firmware_version
    )
