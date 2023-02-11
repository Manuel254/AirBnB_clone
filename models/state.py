#!usr/bin/python3
"""This module contains the class State that defines a state"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class defines a template of creating a state
    Args:
        name (str): name of state
    """

    name = ""
