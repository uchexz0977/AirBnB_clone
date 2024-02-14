#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User."""

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance."""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")

    def to_dict(self):
        """Return a dictionary representation of the User instance."""
        user_dict = super().to_dict()
        user_dict['email'] = self.email
        user_dict['password'] = self.password
        user_dict['first_name'] = self.first_name
        user_dict['last_name'] = self.last_name
        return user_dict

    def __str__(self):
        """Return the string representation of the User instance."""
        return "[User] ({}) {}: {}".format(self.id, self.email, self.__dict__)

