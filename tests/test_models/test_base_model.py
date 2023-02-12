#!/usr/bin/python3
"""This module handles all test cases related to the class
BaseModel
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This class defines tests cases for the BaseModel
    class
    """

    def setUp(self):
        """Set Up instances"""
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def test_uuid(self):
        """UUID tests"""
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertIsInstance(self.bm1.id, str)
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_instance_type(self):
        """tests what the instance type is"""
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertIsInstance(str(self.bm1), str)

    def test_to_dict(self):
        """tests the dictionary representation of an instance"""
        self.assertIsInstance(self.bm2.to_dict(), dict)
