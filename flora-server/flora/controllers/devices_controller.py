import cherrypy
from config2.config import config
from flora.core import controller_registry, register_get_route, register_put_route, DefaultController
from flora.di import container

class DevicesController(DefaultController):

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

    history_items = container.device_poller_wrapper(tag=device['tag'], poller__mac=device['address']).get_history_items()
    for item in history_items:
      device['newHistoryItems'].append(item.__dict__)

    return device

controller_registry['DevicesController'] = DevicesController()
