#!/usr/bin/python3
import pep8
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.city import City
import sys
import models
import unittest
import json
import os
import datetime


class TestFileStorageMethods(unittest.TestCase):
    """class with tests"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def setUp(self):
        """setting up"""
        self.file = models.storage._FileStorage__file_path

    def tearDown(self):
        """cleaning after"""
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_doc(self):
        """testing docstrings"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_save(self):
        """check if it saves changes"""

        my_model = FileStorage()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(os.path.isfile('file.json'))

    def test_all(self):
        """test method all"""
        my_model = FileStorage()
        my_model_dict = my_model.all()
        self.assertIsNotNone(my_model_dict)
        self.assertEqual(type(my_model_dict), dict)
