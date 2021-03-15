import abc
from flora.models import HistoryItem


class Base(abc.ABC):

  @abc.abstractmethod
  def __init__(self, config: dict = {}):
    self._conn = None

  @abc.abstractmethod
  def add_history_item(self, item: HistoryItem) -> None:
    return None
