#!/usr/bin/python3

"""UnitTests for Review Model"""


import unittest
from uuid import uuid4
from models.review import Review
from time import sleep
from datetime import datetime
from models import storage

class TestReviewModel(unittest.TestCase):
    """Unit Tests for Review Model"""

    def test_is_instance(self):
        review = Review()
        self.assertEqual(Review, type(review))

    def test_no_args(self):
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_id_is_public_str(self):
        review = Review()
        self.assertEqual(str, type(review.id))

    def test_created_at_is_public_datetime(self):
        review = Review()
        self.assertEqual(datetime, type(review.created_at))

    def test_updated_at_is_public_datetime(self):
        review = Review()
        self.assertEqual(datetime, type(review.updated_at))

    def test_place_id_is_public_str(self):
        review = Review()
        self.assertEqual(str, type(review.place_id))

    def test_user_id_is_public_str(self):
        review = Review()
        self.assertEqual(str, type(review.user_id))

    def test_text_is_public_str(self):
        review = Review()
        self.assertEqual(str, type(review.text))

    def test_new_instance_in_file_object(self):
        review = Review()
        self.assertIn("{}.{}".format(review.__class__.__name__, review.id), storage.all().keys())
        self.assertIn(review, storage.all().values())

    def test_review_unique_uuid(self):
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_different_created_at(self):
        review1 = Review()
        sleep(0.1)
        review2 = Review()
        self.assertNotEqual(review1.created_at, review2.created_at)

    def test_different_updated_at(self):
        review1 = Review()
        sleep(0.1)
        review2 = Review()
        self.assertNotEqual(review1.updated_at, review2.updated_at)

    def test_with_kwargs(self):
        now = datetime.now()
        temp_id = str(uuid4())
        model = Review(id=temp_id, created_at=now.isoformat(), updated_at=now.isoformat())
        self.assertEqual(model.id, temp_id)
        self.assertEqual(model.created_at, now)
        self.assertEqual(model.updated_at, now)
        
if __name__ == "__main__":
    unittest.main()