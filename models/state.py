#!/usr/bin/python3
"""This holds the State class"""
import models as m
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the Representation of state"""
    if m.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """This initializes the state"""
        super().__init__(*args, **kwargs)

    if m.storage_t != "db":
        @property
        def cities(self):
            """
                This is the getter for list of city
                instances related to the state
            """
            city_list = []
            all_cities = m.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
