from miflora.miflora_poller import MiFloraPoller
from ..models import HistoryItem
from ..pollers import BasePoller
from typing import List


class MiPoller(BasePoller):

  def __init__(self, tag: str, poller: MiFloraPoller):
    super(self.__class__, self).__init__(tag)
    self._poller = poller

  def get_history_items(self, clear: bool = False) -> List[HistoryItem]:
    items = []
    for item in self._poller.fetch_history():
      items.append(HistoryItem(plant_tag=self._tag,
                               address=self._poller._mac,
                               entry=item,
                               batery_level=self._poller.battery_level(),
                               firmware_version=self._poller._firmware_version))
    if clear:
      self._poller.clear_history()
    return items
