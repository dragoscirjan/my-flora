"""Testing flora.di"""

import sqlite3
import unittest
from flora.db import Base as DbBase, Sqlite
from flora.controllers import Base as ControllerBase, DevicesController
from flora.di import Container
from flora.routes import RouteDispatcher

class DITestCase(unittest.TestCase):
  """`di` Test Case"""

  def setUp(self) -> None:
    self.container = Container()
    self.container.config.from_dict({
      'sqlite_or_none': 'sqlite',
      'db': {
        'config': {
          'database': 'my_flora.sqlite'
        }
      }
    })

  def test_db_adapter(self):
    """Testing `db_adapter` to be initialized"""
    db_adapter = self.container.db_adapter()
    self.assertIsInstance(db_adapter, DbBase)
    self.assertIsInstance(db_adapter, Sqlite)
    self.assertIsInstance(db_adapter._conn, sqlite3.Connection)
    self.assertEqual(True, True)

  def test_devices_controller(self):
    """Testing `devices_controller` to be initialized"""
    devices_controller = self.container.devices_controller()
    self.assertIsInstance(devices_controller, ControllerBase)
    self.assertIsInstance(devices_controller, DevicesController)
    self.assertIsInstance(devices_controller._db_adapter, Sqlite)

  def test_route_dispatcher(self):
    """Testing `route_dispatcher` to be initialized"""
    route_dispatcher = self.container.route_dispatcher()
    self.assertIsInstance(route_dispatcher, RouteDispatcher)
    self.assertIsInstance(route_dispatcher._controllers['DevicesController'], DevicesController)
