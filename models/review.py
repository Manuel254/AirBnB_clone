#!usr/bin/python3
"""This module contains the class Review that defines a review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a template of creating a review
    Args:
        place_id (str): Place.id
        user_id (str): User.id
        text (str): review to be written
    """

    place_id = ""
    user_id = ""
    text = ""
