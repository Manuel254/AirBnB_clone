#!usr/bin/python3
"""This module contains the class City that defines a city"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class defines a template of creating a city
    Args:
        state_id (str): State.id
        name (str): name of city
    """

    state_id = ""
    name = ""
