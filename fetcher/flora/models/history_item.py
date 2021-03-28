from miflora.miflora_poller import HistoryEntry
from datetime import datetime
import math

class HistoryItem(dict):

  def __init__(self, **kwargs):
    for key in  ['address', 'plant_tag', 'batery_level', 'firmware_version']:
      if key not in kwargs:
        raise Exception('`{key}` must be present'.format(key=key))
    if 'entry' in kwargs:
      if not isinstance(kwargs['entry'], HistoryEntry):
        raise Exception('`entry` must be instance of HistoryEntry')
    else:
      for key in ['device_time', 'temperature', 'light', 'moisture', 'conductivity']:
        if key not in kwargs:
          raise Exception('`{key}` must be present'.format(key=key))

    for key in ['address', 'plant_tag', 'device_time', 'temperature', 'light', 'moisture', 'conductivity',
                'batery_level', 'firmware_version']:
      if key in kwargs:
        self[key] = kwargs[key]

    if 'entry' in kwargs:
      self['device_time'] = math.trunc(kwargs['entry'].wall_time.timestamp())
      self['temperature'] = kwargs['entry'].temperature
      self['light'] = kwargs['entry'].light
      self['moisture'] = kwargs['entry'].moisture
      self['conductivity'] = kwargs['entry'].conductivity
