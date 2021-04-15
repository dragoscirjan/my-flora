import abc
from ..models import HistoryItem
from typing import List, Type

class BasePoller:

    def __init__(self, tag: str, **kwargs):
        self._tag = tag
        self._kwargs = kwargs

    @abc.abstractmethod
    def get_history_items(self, clear: bool = False) -> List[HistoryItem]:
        pass

    def get_last_history_item(self, clear: bool = False):
        return self.get_history_items(clear)[0]

class PollerFactory:

    @staticmethod
    def get_instance(klass: Type[BasePoller], tag: str, **kwargs) -> BasePoller:
        return klass(tag, **kwargs)
