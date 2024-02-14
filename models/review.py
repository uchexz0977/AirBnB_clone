#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review."""

    def __init__(self, *args, **kwargs):
        """Initialize a new Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")

    def to_dict(self):
        """Return a dictionary representation of the Review instance."""
        review_dict = super().to_dict()
        review_dict.update({
            'place_id': self.place_id,
            'user_id': self.user_id,
            'text': self.text,
        })
        return review_dict

    def __str__(self):
        """Return the string representation of the Review instance."""
        return "[Review] ({}) {}".format(self.id, self.__dict__)

