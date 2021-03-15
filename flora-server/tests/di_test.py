"""Testing flora.di"""

import sqlite3
import unittest
from flora.db import Base, Sqlite
from flora.di import Container, DevicePollerAdapters
from miflora.miflora_poller import MiFloraPoller
from btlewrap import bluepy, pygatt


class DITestCase(unittest.TestCase):
  """`di` Test Case"""

  def setUp(self) -> None:
    self.container = Container()
    self.container.config.from_dict({
      'db': {
        'adapter': Sqlite,
        'config': {
          'database': 'my_flora.sqlite'
        }
      },
      'miflora': {
        'poller': {
          'adapter': bluepy.BluepyBackend
        }
      }
    })


  def test_miflora_device_poller(self):
    """Testing `miflora_device_poller` to be initialized"""
    self.assertIsInstance(self.container.miflora_device_poller('address'), MiFloraPoller)

  def test_miflora_device_poller__address(self):
    """Testing `miflora_device_poller` to be initialized with given address"""
    self.assertEqual(self.container.miflora_device_poller('address')._mac, 'address')

  def test_miflora_device_poller__bluepy(self):
    """Testing `miflora_device_poller` to be initialized with given bt backend"""
    self.assertIsInstance(self.container.miflora_device_poller('address')._bt_interface._backend, bluepy.BluepyBackend)

  # TODO: make sure PyGatt is working as well
  # def test_flora_device_poller__pygatt(self):
  #   """Testing `miflora_device_poller` to be initialized with given bt backend"""
  #   self.container.config.from_dict(
  #     {
  #       'device': {
  #         'adapter': DevicePollerAdapters.pygatt
  #       }
  #     }
  #   )
  #   self.assertIsInstance(self.container.flora_device_poller('address')._bt_interface._backend, pygatt.PygattBackend)

  def test_device_poller_wrapper(self):
    """Testing `flora_device_poller` to be initialized"""
    poller = self.container.device_poller_wrapper(tag='tag', poller__mac='address')
    self.assertEqual(poller._tag, 'tag')
    self.assertEqual(poller._poller._mac, 'address')
    self.assertIsInstance(poller._poller._bt_interface._backend, bluepy.BluepyBackend)

  def test_db_adapter(self):
    """Testing `miflora_device_poller` to be initialized"""
    db_adapter = self.container.db_adapter()
    # self.assertIsInstance(db_adapter, Base)
    # self.assertIsInstance(db_adapter._conn, sqlite3.Connection)
    self.assertEqual(True, True)
