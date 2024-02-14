#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity."""

    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")

    def to_dict(self):
        """Return a dictionary representation of the Amenity instance."""
        amenity_dict = super().to_dict()
        amenity_dict.update({
            'name': self.name,
        })
        return amenity_dict

    def __str__(self):
        """Return the string representation of the Amenity instance."""
        return "[Amenity] ({}) {}".format(self.id, self.__dict__)

