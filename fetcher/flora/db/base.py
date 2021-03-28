import abc
from flora.models import HistoryItem
from typing import List


class Base(abc.ABC):

  @abc.abstractmethod
  def __init__(self, config: dict = {}):
    pass

  @abc.abstractmethod
  def add_history_item(self, item: HistoryItem = None) -> None:
    pass

  @abc.abstractmethod
  def get_history_items(self, address: str) -> List[HistoryItem]:
    pass

  @abc.abstractmethod
  def get_latest_history_item(self, address: str) -> HistoryItem:
    pass
