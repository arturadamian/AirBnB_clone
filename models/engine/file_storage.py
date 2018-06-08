#!/usr/bin/python3
"""creating a file storage"""
import json
#import os

class FileStorage:
    """a new class that serializes instances to a JSON file and back"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        """constructor"""
        pass
    
    def all(self):
        """"""
        return self.__objects

    def new(self, obj):
        """"""
        self.__objects[obj.__class__.__name__ + obj.id] = obj

    def save(self):
        """"""
        with open(type(self).__file_path, "w") as f:
            f.write(json.dumps(type(self).__objects))

    def reload(self):
        """"""
        try:
            with open(type(self).__file_path, "r") as f:
                json.loads(f)
        except:
            pass
        #       if os.path.isfile(type(self).__file_path):
