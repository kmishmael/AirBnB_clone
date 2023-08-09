#!/usr/bin/python3

"""UnitTests for Amenity Model"""


import unittest
from uuid import uuid4
from models.amenity import Amenity
from time import sleep
from datetime import datetime
from models import storage

class TestAmenityModel(unittest.TestCase):
    """Unit Tests for Amenity Model"""

    def test_is_instance(self):
        amenity = Amenity()
        self.assertEqual(Amenity, type(amenity))

    def test_no_args(self):
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_id_is_public_str(self):
        amenity = Amenity()
        self.assertEqual(str, type(amenity.id))

    def test_created_at_is_public_datetime(self):
        amenity = Amenity()
        self.assertEqual(datetime, type(amenity.created_at))

    def test_updated_at_is_public_datetime(self):
        amenity = Amenity()
        self.assertEqual(datetime, type(amenity.updated_at))

    def test_name_is_public_str(self):
        amenity = Amenity()
        self.assertEqual(str, type(amenity.name))

    def test_new_instance_in_file_object(self):
        amenity = Amenity()
        self.assertIn("{}.{}".format(amenity.__class__.__name__, amenity.id), storage.all().keys())
        self.assertIn(amenity, storage.all().values())

    def test_amenity_unique_uuid(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_different_created_at(self):
        amenity1 = Amenity()
        sleep(0.1)
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.created_at, amenity2.created_at)

    def test_different_updated_at(self):
        amenity1 = Amenity()
        sleep(0.1)
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.updated_at, amenity2.updated_at)

    def test_with_kwargs(self):
        now = datetime.now()
        temp_id = str(uuid4())
        model = Amenity(id=temp_id, created_at=now.isoformat(), updated_at=now.isoformat())
        self.assertEqual(model.id, temp_id)
        self.assertEqual(model.created_at, now)
        self.assertEqual(model.updated_at, now)
        
if __name__ == "__main__":
    unittest.main()