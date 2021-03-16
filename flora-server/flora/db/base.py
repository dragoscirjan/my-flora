import abc
from flora.models import HistoryItem


class Base(abc.ABC):

  @abc.abstractmethod
  def __init__(self, config: dict = {}):
    pass

  @abc.abstractmethod
  def add_history_item(self, item: HistoryItem = None) -> None:
    pass

  @abc.abstractmethod
  def get_latest_history_item(self, address: str) -> HistoryItem:
    pass
