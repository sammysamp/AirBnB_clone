#!/usr/bin/python3
"""module for testing user class"""
import unittest
from datetime import datetime
from time import sleep
from models.city import City
from models.base_model import BaseModel
from unittest.mock import patch
import pycodestyle
import models
# import pep8


class Test_PEP8(unittest.TestCase):
    """test User"""

    def test_pep8_user(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_docstrings(unittest.TestCase):

    @classmethod
    def setup_class(self):
        """Setup for docstring"""
        self.user_1 = City()

    def test_docstrings(self):
        """test documentation"""
        self.assertIsNotNone(City.__doc__, "city.py needs a docstring")


class test_inherit_basemodel(unittest.TestCase):
    """Test if user inherit from BaseModel"""
    def test_instance(self):
        """check if user is an instance of BaseModel"""
        user = City()
        self.assertIsInstance(user, City)
        self.assertTrue(issubclass(type(user), BaseModel))
        self.assertEqual(str(type(user)), "<class 'models.city.City'>")


class test_Amenity_BaseModel(unittest.TestCase):
    """Testing City class"""
    def test_instances(self):
        with patch('models.city'):
            instance = City()
            self.assertEqual(type(instance), City)
            instance.name = "OnePiece"
            instance.state_id = "3344-SiliconValley"
            expectec_attrs_types = {
                    "id": str,
                    "created_at": datetime,
                    "updated_at": datetime,
                    "name": str,
                    "state_id": str
                    }
            inst_dict = instance.to_dict()
            expected_dict_attrs = [
                    "id",
                    "created_at",
                    "updated_at",
                    "name",
                    "state_id",
                    "__class__"
                    ]
            self.assertCountEqual(inst_dict.keys(), expected_dict_attrs)
            self.assertEqual(inst_dict['name'], 'OnePiece')
            self.assertEqual(inst_dict['state_id'], '3344-SiliconValley')
            self.assertEqual(inst_dict['__class__'], 'City')

            for attr, types in expectec_attrs_types.items():
                with self.subTest(attr=attr, typ=types):
                    self.assertIn(attr, instance.__dict__)
                    self.assertIs(type(instance.__dict__[attr]), types)
            self.assertEqual(instance.name, "OnePiece")
            self.assertEqual(instance.state_id, "3344-SiliconValley")

    def test_City_id_and_createat(self):
        """testing id for every user"""
        user_1 = City()
        sleep(2)
        user_2 = City()
        sleep(2)
        user_3 = City()
        sleep(2)
        list_users = [user_1, user_2, user_3]
        for instance in list_users:
            user_id = instance.id
            with self.subTest(user_id=user_id):
                self.assertIs(type(user_id), str)
        self.assertNotEqual(user_1.id, user_2.id)
        self.assertNotEqual(user_1.id, user_3.id)
        self.assertNotEqual(user_2.id, user_3.id)
        self.assertTrue(user_1.created_at <= user_2.created_at)
        self.assertTrue(user_2.created_at <= user_3.created_at)
        self.assertNotEqual(user_1.created_at, user_2.created_at)
        self.assertNotEqual(user_1.created_at, user_3.created_at)
        self.assertNotEqual(user_3.created_at, user_2.created_at)

    def test_str_method(self):
        """
        Testin str magic method
        """
        inst = City()
        str_output = "[City] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(str_output, str(inst))

    @patch('models.storage')
    def test_save_method(self, mock_storage):
        """Testing save method and if it update"""
        instance5 = City()
        created_at = instance5.created_at
        sleep(2)
        updated_at = instance5.updated_at
        instance5.save()
        new_created_at = instance5.created_at
        sleep(2)
        new_updated_at = instance5.updated_at
        self.assertNotEqual(updated_at, new_updated_at)
        self.assertEqual(created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)
x
if __name__ == '__main__':
    unittest.main()
