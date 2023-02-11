#!usr/bin/python3
"""This module contains the class Place that defines a place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This class defines a template of creating a place
    Args:
        city_id (str): City.id
        user_id (str): User.id
        name (str): name of place
        description (str): description of place
        number_rooms (int): number of rooms in place
        number_bathrooms (int): number of bathrooms in place
        max_guest (int): maximum number of guests
        price_by_night (int): price by night
        latitude (float): latitude position of place
        longitude (float): longitude position of place
        amenity_ids (list): list of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
