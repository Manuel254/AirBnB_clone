#!usr/bin/python3
"""This module contains the class Amenity that defines the amenities"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class defines a template of creating an amenity
    Args:
        name (str): name of amenity
    """

    name = ""
