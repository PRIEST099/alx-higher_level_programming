#!/usr/bin/python3
"""a unittest for base class"""
import unittest
import os
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """a test class for base class"""

    def test_default_id(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_custom_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_id_increment(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_setting_to_none(self):
        obj = Base(None)
        self.assertEqual(obj.id, 1)

if __name__ == '__main__':
    unittest.main()
