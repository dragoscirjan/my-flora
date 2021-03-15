from copy import deepcopy
import cherrypy
from flora.routes.registry import routes


class RouteDispatcher:

  def __init__(self, controllers: dict = {}):
    self._controllers = controllers

  def build(self) -> cherrypy.dispatch.RoutesDispatcher:
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    for route in routes:
      route = deepcopy(route.__dict__)
      print('route:', route)
      route['controller'] = self._controllers[route['controller']]
      print('route:', route)
      # dispatcher.connect(route['name'], route['route'], route['controller'], **route)
      dispatcher.connect(name=route['name'],
                         route=route['route'],
                         action=route['action'],
                         controller=route['controller'],
                         conditions=route['conditions'])
      print('dispatcher:', dispatcher)

    return dispatcher
