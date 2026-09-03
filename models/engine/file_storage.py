#!/usr/bin/python3
"""Defines the FileStorage class, the JSON persistence engine.

FileStorage is responsible for serializing all in-memory instances to a
JSON file on disk, and deserializing that file back into live objects
when the application starts up again.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes them back.

    Class Attributes:
        __file_path (str): Path to the JSON file used for persistence.
        __objects (dict): Stores all created objects, keyed by
            <class name>.id (e.g. "BaseModel.12121212").
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects containing all stored objects.

        Returns:
            dict: All currently tracked objects, keyed by
                <class name>.<id>.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to __objects, keyed by <obj class name>.id.

        Args:
            obj: The object instance to register with storage.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file at __file_path."""
        serialized = {
            key: obj.to_dict() for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserialize the JSON file at __file_path into __objects.

        If the file does not exist, this method does nothing and does
        not raise an exception.
        """
        classes = {"BaseModel": BaseModel}
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for key, value in data.items():
                cls_name = value["__class__"]
                cls = classes.get(cls_name, BaseModel)
                FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
