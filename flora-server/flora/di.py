from dependency_injector import containers, providers
from btlewrap import bluepy, pygatt
from miflora.miflora_poller import MiFloraPoller
from flora.mi import DevicePollerWrapper

class DevicePollerAdapters:
  bluepy = 'bluepy'
  pygatt = 'pygatt'

def device_poller_backend(adapter: str):
  return bluepy.BluepyBackend if adapter == DevicePollerAdapters.bluepy else \
          pygatt.PygattBackend if adapter == DevicePollerAdapters.pygatt else None

class Container(containers.DeclarativeContainer):

  config = providers.Configuration()

  miflora_device_poller_backend = providers.Callable(
    device_poller_backend,
    config.device.adapter
  )

  miflora_device_poller = providers.Factory(MiFloraPoller)
  miflora_device_poller.add_kwargs(backend=miflora_device_poller_backend)

  device_poller_wrapper = providers.Factory(
    DevicePollerWrapper,
    poller=miflora_device_poller
  )

container = Container()
