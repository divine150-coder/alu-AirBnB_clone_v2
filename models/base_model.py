#!/usr/bin/python3
"""Defines the BaseModel for AirBnB"""

from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """Base model with common attributes and methods for other classes"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance

        Args:
            args: unused positional arguments
            kwargs: key-value pairs to set attributes

        Attributes:
            id: unique identifier
            created_at: instance creation timestamp
            updated_at: last update timestamp
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        return self.__str__()

    def save(self):
        """Update updated_at with current datetime and save the instance"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict.pop('_sa_instance_state', None)
        return my_dict

    def delete(self):
        """Delete the current instance from storage"""
        models.storage.delete(self)
