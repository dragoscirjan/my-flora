import cherrypy
from copy import deepcopy
from flora.controllers import Base as ControllerBase
from flora.routes.registry import routes

class RouteDispatcher:

  def __init__(self, **kwargs):
    self._controllers = {}
    for key in kwargs.keys():
      if isinstance(kwargs.get(key), ControllerBase):
        self._controllers[key] = kwargs.get(key)

  def build(self) -> cherrypy.dispatch.RoutesDispatcher:
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    for route in routes:
      route = deepcopy(route.__dict__)
      route['controller'] = self._controllers[route['controller']]
      dispatcher.connect(name=route['name'],
                         route=route['route'],
                         action=route['action'],
                         controller=route['controller'],
                         conditions=route['conditions'])

    return dispatcher
