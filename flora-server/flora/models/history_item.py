from miflora.miflora_poller import HistoryEntry
from datetime import datetime
import math

class HistoryItem(object):

  def __init__(self, tag: str, entry: HistoryEntry, batery_level: int, firmware_version: str):
    self.plant_tag = tag
    # self.device_time = entry.device_time
    self.device_time = math.trunc(entry.wall_time.timestamp())
    self.temperature = entry.temperature
    self.light = entry.light
    self.moisture = entry.moisture
    self.conductivity = entry.conductivity
    self.batery_level = batery_level
    self.firmware_version = firmware_version
