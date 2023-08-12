#!/usr/bin/python3

"""UnitTests for State Model"""


import unittest
from uuid import uuid4
from models.state import State
from time import sleep
from datetime import datetime
from models import storage


class TestStateModel(unittest.TestCase):
    """Unit Tests for State Model"""

    def test_is_instance(self):
        state = State()
        self.assertEqual(State, type(state))

    def test_no_args(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_id_is_public_str(self):
        state = State()
        self.assertEqual(str, type(state.id))

    def test_created_at_is_public_datetime(self):
        state = State()
        self.assertEqual(datetime, type(state.created_at))

    def test_updated_at_is_public_datetime(self):
        state = State()
        self.assertEqual(datetime, type(state.updated_at))

    def test_name_is_public_str(self):
        state = State()
        self.assertEqual(str, type(state.name))

    def test_new_instance_in_file_object(self):
        state = State()
        self.assertIn("{}.{}".format(state.__class__.__name__, state.id),
                      storage.all().keys())
        self.assertIn(state, storage.all().values())

    def test_state_unique_uuid(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_different_created_at(self):
        state1 = State()
        sleep(0.1)
        state2 = State()
        self.assertNotEqual(state1.created_at, state2.created_at)

    def test_different_updated_at(self):
        state1 = State()
        sleep(0.1)
        state2 = State()
        self.assertNotEqual(state1.updated_at, state2.updated_at)

    def test_with_kwargs(self):
        now = datetime.now()
        temp_id = str(uuid4())
        model = State(id=temp_id, created_at=now.isoformat(),
                      updated_at=now.isoformat())
        self.assertEqual(model.id, temp_id)
        self.assertEqual(model.created_at, now)
        self.assertEqual(model.updated_at, now)


if __name__ == "__main__":
    unittest.main()
