#!/usr/bin/python3
"""Defines the BaseModel class, the parent class for all AirBnB models.

This module provides the BaseModel class which handles the initialization,
serialization, and deserialization of future instances of subclasses used
throughout the project (User, State, City, Amenity, Place, Review, etc).
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class that defines common attributes/methods for all models.

    Every other model in this project (User, State, City, Amenity, Place,
    Review) inherits from this class so they all share the same id,
    timestamps, string representation, and serialization behavior.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args: Unused positional arguments.
            **kwargs: Key/value pairs used to recreate an instance from a
                dictionary representation (as produced by to_dict()). If
                kwargs is empty, a brand-new instance is created instead
                and registered with the storage engine.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel instance.

        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime and persist changes.

        Calls the storage engine's save() method so the change is written
        to the JSON file immediately.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance.

        The returned dictionary contains all keys/values of __dict__,
        plus a __class__ key set to the class name of the instance, and
        with created_at/updated_at converted to ISO format strings so the
        result is JSON-serializable.

        Returns:
            dict: The dictionary representation of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
