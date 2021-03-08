import cherrypy
from flora.core.controller import controller_registry, DefaultController
from flora.core.dict_extend import deepmerge
from typing import Type

cherrypy_routes: list() = []

def build_dispatcher() -> cherrypy.dispatch.RoutesDispatcher:
  dispatcher = cherrypy.dispatch.RoutesDispatcher()

  for route in cherrypy_routes:
    dispatcher.connect(name=route['name'],
                        route=route['route'],
                        action=route['action'],
                        controller=controller_registry[route['controller']],
                        conditions=route['conditions'])

  return dispatcher

def cherrypy_route_append(name: str, route: str, action: str, controller: Type[DefaultController], conditions: dict) -> None:
  route = {
    'name': name,
    'route': route,
    'action': action,
    'controller': controller,
    'conditions': conditions
  }
  cherrypy_routes.append(route)

def register_get_route(name: str, route: str, action: str, controller: Type[DefaultController], conditions: dict = {}):
  def decorator(callable):
    def wrapper(*args, **kwargs):
      return callable(*args, **kwargs)
    new_conditions = deepmerge(conditions, {'method': ['GET']})
    cherrypy_route_append(name=name, route=route, action=action, controller=controller, conditions=new_conditions)
    return wrapper
  return decorator
