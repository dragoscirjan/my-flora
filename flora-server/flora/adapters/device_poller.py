from btlewrap.bluepy import BluepyBackend
from btlewrap.gatttool import GatttoolBackend
from btlewrap.pygatt import PygattBackend
from config2.config import config
from flora.models import HistoryItem
from miflora.miflora_poller import MiFloraPoller

class DevicePoller:

  def __init__(self, address: str):
    if config.device_poller is None:
      raise Exception('No device poller configuration')
    if config.device_poller.adapter is None:
      raise Exception('No device poller adapter present. Accepted values: bluepy, pygatt')
    if config.device_poller.adapter.lower() == 'bluepy':
      self.poller = MiFloraPoller(address, BluepyBackend)
    elif config.device_poller.adapter.lower() == 'pygatt':
      self.poller = MiFloraPoller(address, PygattBackend)
    else:
      raise Exception('Invalid device poller adapter. Accepted values: bluepy, pygatt')

  def get_history_item(self, device_tag: str) -> HistoryItem:
    history = self.poller.fetch_history()
    # self.poller.clear_history()
    return HistoryItem(tag=device_tag,
                        entry=history[0],
                        batery_level=self.poller.battery_level(),
                        firmware_version=self.poller._firmware_version)
