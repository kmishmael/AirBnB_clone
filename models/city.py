#!/usr/bin/python3
"""City model class module"""


from models.base_model import BaseModel

class City(BaseModel):
    """
    City class that inherits from BaseModel.
    
    Public class attributes:
        state_id {string} - empty string
        name {string} - empty string
    """
    state_id = ""
    name = ""
