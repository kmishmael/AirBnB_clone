#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

"""Base model class"""


class BaseModel:
    """
    Representation of Base class. It defines  all common attributes and methods for other classes
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}]"
    
    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict