#!/usr/bin/python3

import unittest
from uuid import uuid4
from models.base_model import BaseModel
from datetime import datetime
import time
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class
    """

    def test_docstrings(self):
        """Test that docstrings are defined
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_instantiation(self):
        """Test if an instance is created"""
        model = BaseModel()
        self.assertEqual(BaseModel, type(model))

    def test_valid_uuid_string(self):
        """Test if uuid is a string
        """
        model = BaseModel()
        self.assertTrue(isinstance(model.id, str))
        self.assertEqual(len(model.id), 36)

    def test_created_at_valid_datetime(self):
        """Test if created_at is a valid datetime
        """
        model = BaseModel()
        self.assertTrue(isinstance(model.created_at, datetime))

    def test_updated_at_valid_datetime(self):
        """Test if updated_at is a valid datetime
        """
        model = BaseModel()
        self.assertTrue(isinstance(model.updated_at, datetime))

    def test_model_uuid_unique(self):
        """Test that uuid generated is `unique`
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_model_created_at(self):
        """Test that two models created at different times are different
        """
        model1 = BaseModel()
        time.sleep(0.1)
        model2 = BaseModel()
        self.assertLess(model1.created_at, model2.created_at)

    def test_models_updated_at(self):
        """Test that the two models updated at is different at
        initialization.
        """
        model1 = BaseModel()
        time.sleep(0.1)
        model2 = BaseModel()
        self.assertLess(model1.updated_at, model2.updated_at)

    def test_str_repr(self):
        """Test that the str representation is correct
        """
        model = BaseModel()
        self.assertIn(model.__class__.__name__, str(model))
        self.assertIn(model.id, str(model))
        self.assertIn(str(model.__dict__), str(model))
        self.assertEqual(
            f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}]",
            str(model))

    def test_new_instance_in_file_object(self):
        model = BaseModel()
        self.assertIn("{}.{}".format(model.__class__.__name__, model.id),
                      storage.all().keys())
        self.assertIn(model, storage.all().values())

    def test_save_updates_updated_at(self):
        """Test if saving updates updated_at
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_returns_dict(self):
        """Test the `to_dict()` actually returns a <class dict>"""
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))

    def test_to_dict_contains_expected_keys(self):
        """Test that the dictionary contains expected keys"""
        model = BaseModel()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        obj_dict = model.to_dict()
        for key in expected_keys:
            self.assertIn(key, obj_dict)

    def test_with_kwargs(self):
        now = datetime.now()
        temp_id = str(uuid4())
        model = BaseModel(id=temp_id, created_at=now.isoformat(),
                          updated_at=now.isoformat())
        self.assertEqual(model.id, temp_id)
        self.assertEqual(model.created_at, now)
        self.assertEqual(model.updated_at, now)


if __name__ == '__main__':
    unittest.main()
