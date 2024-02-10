#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tday = "Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(value, tday)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the str rep of BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at the current time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dict of BaseModel instance """
        odict = self.__dict__.copy()
        odict['__class__'] = self.__class__.__name__
        odict['created_at'] = self.created_at.isoformat()
        odict['updated_at'] = self.updated_at.isoformat()
        return odict
