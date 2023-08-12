#!/usr/bin/python3
"""Review model class module"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Public class attributes:
        place_id {string} - empty string
        user_id {string} - empty string
        text {string} - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
