from config2.config import config as file_config
from dependency_injector import containers, providers
from btlewrap import bluepy, pygatt
from miflora.miflora_poller import MiFloraPoller
from flora.mi import DevicePollerWrapper

file_config.get()

class DevicePollerAdapters:
  bluepy = 'bluepy'
  pygatt = 'pygatt'

def device_poller_backend(adapter: str):
  return bluepy.BluepyBackend if adapter == DevicePollerAdapters.bluepy else \
          pygatt.PygattBackend if adapter == DevicePollerAdapters.pygatt else None

class Container(containers.DeclarativeContainer):

  config = providers.Configuration()

  miflora_device_poller = providers.Factory(
    MiFloraPoller,
    backend=config.miflora.poller.adapter
  )

  device_poller_wrapper = providers.Factory(
    DevicePollerWrapper,
    poller=miflora_device_poller
  )


bt_adapter = file_config.miflora.poller.adapter

container = Container()
container.config.from_dict({
  'miflora': {
    'poller': {
      'adapter': bluepy.BluepyBackend if not bt_adapter or bt_adapter.lower() == 'bluepy'\
                  else pygatt.PygattBackend if bt_adapter.lower() == 'pygatt' else None
    }
  }
})
