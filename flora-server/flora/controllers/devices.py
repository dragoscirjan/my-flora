import cherrypy
from config2.config import config
from dependency_injector import providers
from flora.controllers import Base
from flora.mi import container as mi_container
from flora.routes.registry import register_get_route, register_put_route

class DevicesController(Base):

  def __init__(self, db_adapter: providers.Singleton):
    self._db_adapter = db_adapter

  @cherrypy.tools.json_out()
  @register_get_route(name='devices', route='/v1/devices', action='get_devices', controller='DevicesController')
  def get_devices(self):
    return config.devices

  @cherrypy.tools.json_out()
  @register_get_route(name='device_details', route='/v1/devices/{address}',
                      action='get_device_details', controller='DevicesController')
  def get_device_details(self, address: str) -> dict:
    found = None
    for device in config.devices:
      if device['address'] == address:
        found = device

    if found is None:
      raise cherrypy.HTTPError(404, 'Invalid device with mac address: {}'.format(address))

    return found

  @cherrypy.tools.json_out()
  @register_put_route(name='device_interrogate', route='/v1/devices/{address}',
                      action='put_device_details', controller='DevicesController')
  def put_device_details(self, address: str) -> dict:
    device = self.get_device_details(address=address)
    device['newHistoryItems'] = []

    print('db_adapter:', self._db_adapter)

    latest_item = self._db_adapter.get_latest_history_item(address=address)

    poller = mi_container.device_poller_wrapper(tag=device['tag'], poller__mac=device['address'])
    for item in poller.get_history_items():
      if latest_item is None or latest_item['device_time'] < item['device_time']:
        self._db_adapter.add_history_item(item=item)
      device['newHistoryItems'].append(item)

    return device
