#!/usr/bin/python3

"""UnitTests for City Model"""


import unittest
from uuid import uuid4
from models.city import City
from time import sleep
from datetime import datetime
from models import storage


class TestCityModel(unittest.TestCase):
    """Unit Tests for City Model"""

    def test_is_instance(self):
        city = City()
        self.assertEqual(City, type(city))

    def test_no_args(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_id_is_public_str(self):
        city = City()
        self.assertEqual(str, type(city.id))

    def test_created_at_is_public_datetime(self):
        city = City()
        self.assertEqual(datetime, type(city.created_at))

    def test_updated_at_is_public_datetime(self):
        city = City()
        self.assertEqual(datetime, type(city.updated_at))

    def test_state_id_is_public_str(self):
        city = City()
        self.assertEqual(str, type(city.state_id))

    def test_name_is_public_str(self):
        city = City()
        self.assertEqual(str, type(city.name))

    def test_new_instance_in_file_object(self):
        city = City()
        self.assertIn("{}.{}".format(city.__class__.__name__, city.id),
                      storage.all().keys())
        self.assertIn(city, storage.all().values())

    def test_city_unique_uuid(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_different_created_at(self):
        city1 = City()
        sleep(0.1)
        city2 = City()
        self.assertNotEqual(city1.created_at, city2.created_at)

    def test_different_updated_at(self):
        city1 = City()
        sleep(0.1)
        city2 = City()
        self.assertNotEqual(city1.updated_at, city2.updated_at)

    def test_with_kwargs(self):
        now = datetime.now()
        temp_id = str(uuid4())
        model = City(id=temp_id, created_at=now.isoformat(),
                     updated_at=now.isoformat())
        self.assertEqual(model.id, temp_id)
        self.assertEqual(model.created_at, now)
        self.assertEqual(model.updated_at, now)


if __name__ == "__main__":
    unittest.main()
