from typing import List
from config2.config import config
from flora.models import HistoryItem
from miflora.miflora_poller import MiFloraPoller

class DevicePollerWrapper:

  def __init__(self, tag: str, poller: MiFloraPoller):
    self._poller = poller
    self._tag = tag

  def get_history_items(self) -> List[HistoryItem]:
    history = self._poller.fetch_history()
    items = []
    for item in history:
      items.append(HistoryItem(tag=self._tag,
                                entry=history[0],
                                batery_level=self._poller.battery_level(),
                                firmware_version=self._poller._firmware_version))
    if config.device.poller.history.clear:
      self._poller.clear_history()
    return items

  def get_last_history_item(self):
    return self.get_history_items()[0]
