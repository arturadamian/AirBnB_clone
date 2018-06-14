#!/usr/bin/python3
"""tests place class
"""

from models.place import Place
import pep8
import os
import unittest


class TestPlace(unittest.TestCase):
    """tests Place"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstrings(self):
        """testing docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_hasattribute(self):
        """test attributes"""
        my_model = Place()
        self.assertTrue(hasattr(my_model, "__init__"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "id"))
