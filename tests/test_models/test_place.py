#!/usr/bin/python3

"""UnitTests for Place Model"""


import unittest
from uuid import uuid4
from models.place import Place
from time import sleep
from datetime import datetime
from models import storage

class TestPlaceModel(unittest.TestCase):
    """Unit Tests for Place Model"""

    def test_is_instance(self):
        place = Place()
        self.assertEqual(Place, type(place))

    def test_no_args(self):
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_id_is_public_str(self):
        place = Place()
        self.assertEqual(str, type(place.id))

    def test_created_at_is_public_datetime(self):
        place = Place()
        self.assertEqual(datetime, type(place.created_at))

    def test_updated_at_is_public_datetime(self):
        place = Place()
        self.assertEqual(datetime, type(place.updated_at))

    def test_city_id_is_public_str(self):
        place = Place()
        self.assertEqual(str, type(place.city_id))

    def test_user_id_is_public_str(self):
        place = Place()
        self.assertEqual(str, type(place.user_id))

    def test_name_is_public_str(self):
        place = Place()
        self.assertEqual(str, type(place.name))

    def test_description_is_public_str(self):
        place = Place()
        self.assertEqual(str, type(place.description))

    def test_number_rooms_is_public_str(self):
        place = Place()
        self.assertEqual(str, type(place.number_rooms))

    def test_number_bathrooms_is_public_str(self):
        place = Place()
        self.assertEqual(str, type(place.number_bathrooms))

    def test_max_guest_is_public_str(self):
        place = Place()
        self.assertEqual(str, type(place.max_guest))

    def test_price_by_night_is_public_str(self):
        place = Place()
        self.assertEqual(str, type(place.price_by_night))

    def test_latitude_is_public_str(self):
        place = Place()
        self.assertEqual(str, type(place.latitude))

    def test_longitude_is_public_str(self):
        place = Place()
        self.assertEqual(str, type(place.longitude))

    def test_amenity_ids_is_public_str(self):
        place = Place()
        self.assertEqual(str, type(place.amenity_ids))

    def test_new_instance_in_file_object(self):
        place = Place()
        self.assertIn("{}.{}".format(place.__class__.__name__, place.id), storage.all().keys())
        self.assertIn(place, storage.all().values())

    def test_place_unique_uuid(self):
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_different_created_at(self):
        place1 = Place()
        sleep(0.1)
        place2 = Place()
        self.assertNotEqual(place1.created_at, place2.created_at)

    def test_different_updated_at(self):
        place1 = Place()
        sleep(0.1)
        place2 = Place()
        self.assertNotEqual(place1.updated_at, place2.updated_at)

    def test_with_kwargs(self):
        now = datetime.now()
        temp_id = str(uuid4())
        model = Place(id=temp_id, created_at=now.isoformat(), updated_at=now.isoformat())
        self.assertEqual(model.id, temp_id)
        self.assertEqual(model.created_at, now)
        self.assertEqual(model.updated_at, now)
        

if __name__ == "__main__":
    unittest.main()