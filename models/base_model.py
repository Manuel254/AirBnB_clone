#!usr/bin/python3
"""This is the Base Model class module"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """This class defines all common attributes/
    methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes an instance
        Args:
            *args (any): anonymous arguments
            **kwargs (any): keyword arguments
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    setattr(
                            self,
                            key,
                            datetime.strptime(
                                        value,
                                        "%Y-%m-%dT%H:%M:%S.%f"
                                        )
                            )
                elif key == 'updated_at':
                    setattr(
                            self,
                            key,
                            datetime.strptime(
                                        value,
                                        "%Y-%m-%dT%H:%M:%S.%f"
                                        )
                            )
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates the public instance attribute
        with current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dict = {
                    **self.__dict__,
                    **{"__class__": self.__class__.__name__}
                    }
        new_dict["created_at"] = new_dict[
                                        "created_at"
                                        ].strftime(
                                                "%Y-%m-%dT%H:%M:%S.%f"
                                                )

        new_dict["updated_at"] = new_dict[
                                        "updated_at"
                                        ].strftime(
                                                "%Y-%m-%dT%H:%M:%S.%f"
                                                )

        return new_dict

    def __str__(self):
        """Prints an instance in a readable format"""
        return "[{}] ({}) {}".format(
                                    self.__class__.__name__,
                                    self.id,
                                    self.__dict__
                                    )
