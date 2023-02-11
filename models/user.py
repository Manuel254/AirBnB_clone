#!usr/bin/python3
"""This module contains the class User that defines a user"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a template of creating a user
    Args:
        email (str): email of user
        password (str): password of user
        first_name (str): first name of user
        last_name (str): last name of user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
