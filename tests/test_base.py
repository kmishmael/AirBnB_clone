import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class
    """

    def test_valid_uuid_string(self):
        model = BaseModel()
        self.assertTrue(isinstance(model.id, str))
        self.assertEqual(len(model.id), 36)
    
    def test_valid_datetime(self):
        model = BaseModel()
        self.assertTrue(isinstance(model.created_at, datetime))
        self.assertTrue(isinstance(model.updated_at, datetime))

    def test_uuid_not_equal(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_str_representation(self):
        model = BaseModel()
        self.assertIn(model.__class__.__name__, str(model))
        self.assertIn(model.id, str(model))

    def test_save_updates_updated_at(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_returns_dict(self):
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))

    def test_to_dict_contains_expected_keys(self):
        model = BaseModel()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        obj_dict = model.to_dict()
        for key in expected_keys:
            self.assertIn(key, obj_dict)

if __name__ == '__main__':
    unittest.main()