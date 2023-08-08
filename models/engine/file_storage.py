#!/usr/bin/python3
"""File Storage Definition"""


import json
from models.base_model import BaseModel

class FileStorage:
    """Representation of file storage
    """
    __file_path = 'file.json'
    __objects = {}
    def __init__(self):
        """Instance initialization
        """
        pass

    def all(self):
        """
        get dict object
        
        Returns:
            objects {__objects}
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        sets in `__objects` object with key `<obj class name>.id`
        Args:
            obj {object} - object to be created
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        """
        Serialize `objects` to the JSON file
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to `objects` if it exists, else FileNotFoundError
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    obj = cls(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass

    
