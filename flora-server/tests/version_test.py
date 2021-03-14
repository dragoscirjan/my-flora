"""Testing flora.version"""

import unittest
from flora.version import get_static_version


class VersionTestCase(unittest.TestCase):
  """`get_static_version` Test Case"""

  def test_get_static_version(self):
    """Testing `get_static_version` returns proper value"""
    self.assertEqual(get_static_version(), '0.0.1')
