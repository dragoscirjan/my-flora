"""Testing flora.hello"""

# ##
# Model for using Pytest
# ##

# import pytest
# from flora.hello import hello

# def test_hello():
#   assert hello('World') == 'Hello World!'


###
# Model for using UnitTest
###

import unittest
from flora.hello import hello


class HelloTestCase(unittest.TestCase):
  """`hello` Test Case"""

  def test_hello(self):
    """Testing `hello` returns proper message"""
    self.assertEqual(hello('World'), 'Hello World!')
