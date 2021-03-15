from typing import List
from flora.core.dict_extend import deepmerge


class Route:

  def __init__(self, name: str, route: str, action: str, controller: str, conditions: dict = {}):
    if type(name) is dict:
      self.name = name.get('name')
      self.route = name.get('route')
      self.action = name.get('action')
      self.controller = name.get('controller')
      self.conditions = name.get('conditions')
    else:
      self.name = name
      self.route = route
      self.action = action
      self.controller = controller
      self.conditions = conditions


class Routes:

  def __init__(self):
    self._registry: List[Route] = []

  def add_route(self, name: str, route: str, action: str, controller: str, conditions: dict = {}) -> None:
    self._registry.append(Route(name, route, action, controller, conditions))

  def __iter__(self):
    self._index = 0
    return self

  def __next__(self):
    if self._index < len(self._registry):
      item = self._registry[self._index]
      self._index += 1
      return item
    raise StopIteration


routes = Routes()


def register_get_route(name: str, route: str, action: str, controller: str, conditions: dict = {}):
  def decorator(callable):
    new_conditions = deepmerge(conditions, {'method': ['GET']})
    routes.add_route(name=name, route=route, action=action, controller=controller,
                     conditions=new_conditions)

    def wrapper(*args, **kwargs):
      return callable(*args, **kwargs)

    return wrapper

  return decorator


def register_put_route(name: str, route: str, action: str, controller: str, conditions: dict = {}):
  def decorator(callable):
    new_conditions = deepmerge(conditions, {'method': ['PUT']})
    routes.add_route(name=name, route=route, action=action, controller=controller,
                     conditions=new_conditions)

    def wrapper(*args, **kwargs):
      return callable(*args, **kwargs)

    return wrapper

  return decorator
