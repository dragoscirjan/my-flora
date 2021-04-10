import collections
from copy import deepcopy

def deepmerge(dict1, dict2):
  result = deepcopy(dict1)

  for key, value in dict2.items():
    if isinstance(value, collections.Mapping):
      result[key] = merge(result.get(key, {}), value)
    else:
      result[key] = deepcopy(dict2[key])

  return result
