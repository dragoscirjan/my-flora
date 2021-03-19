import sqlite3
from flora.db import Base
from flora.models import HistoryItem
from typing import List


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

    conn = sqlite3.connect(**self._config)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

  def get_history_items(self, address: str) -> List[HistoryItem]:
    query = '''
  SELECT * FROM history_items hi WHERE hi.address = '{address}' ORDER BY hi.device_time DESC LIMIT 0, 100
'''.format(address=address)

    cursor = sqlite3.connect(**self._config).cursor()
    cursor.execute(query)

    history_items = []
    for item in cursor.fetchall():
      (id,
       address,
       plant_tag,
       device_time,
       temperature,
       light,
       moisture,
       conductivity,
       batery_level,
       firmware_version) = item
      history_items.append(HistoryItem(
        address=address,
        plant_tag=plant_tag,
        device_time=device_time,
        temperature=temperature,
        light=light,
        moisture=moisture,
        conductivity=conductivity,
        batery_level=batery_level,
        firmware_version=firmware_version
      ))

    cursor.close()

    return history_items

  def get_latest_history_item(self, address: str) -> HistoryItem:
    query = '''
  SELECT * FROM history_items hi WHERE hi.address = '{address}' ORDER BY hi.device_time DESC LIMIT 0, 1
'''.format(address=address)

    cursor = sqlite3.connect(**self._config).cursor()
    cursor.execute(query)

    last_item = cursor.fetchone()

    if last_item is None:
      return None

    (id,
     address,
     plant_tag,
     device_time,
     temperature,
     light,
     moisture,
     conductivity,
     batery_level,
     firmware_version) = last_item
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
