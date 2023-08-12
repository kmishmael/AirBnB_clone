#!/usr/bin/python3
"""Place model class module"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.

    Public class attributes:
        city_id {string} - empty string
        user_id {string} - empty string
        name {string} - empty string
        description {string} - empty string
        number_rooms {string} - empty string
        number_bathrooms {string} - empty string
        max_guest {string} - empty string
        price_by_night {string} - empty string
        latitude {string} - empty string
        longitude {string} - empty string
        amenity_ids {string} - empty string`1
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
