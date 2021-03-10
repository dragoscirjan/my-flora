from config2.config import config
import cherrypy
from flora.core import controller_registry, register_get_route, DefaultController

class DevicesController(DefaultController):

  @cherrypy.tools.json_out()
  @register_get_route(name='devices', route='/v1/devices', action='get_devices', controller='DevicesController')
  def get_devices(self):
    return config.devices

  @cherrypy.tools.json_out()
  @register_get_route(name='devices', route='/v1/devices/{address}',
                      action='get_device_details', controller='DevicesController')
  def get_device_details(self, address: str) -> dict:
    found = None
    for device in config.devices:
      if device['address'] == address:
        found = device

    if found is None:
      raise cherrypy.HTTPError(404, 'Invalid device with mac address: {}'.format(address))

    return found

controller_registry['DevicesController'] = DevicesController()
