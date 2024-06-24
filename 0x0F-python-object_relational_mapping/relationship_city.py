#!/usr/bin/python3

"""
    This module contains a Base class and the City class which inherits from Base.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import relationship


# Base class that provides a common base for declarative class definitions
Base = declarative_base()


class City(Base):
    """
    City class that inherits from Base class.

    Attributes:
        id (int): Primary key for the city.
        name (string): Name of the city.
        state_id (string): Foreign key to the state table.
    """

    # Table name for the City class
    __tablename__ = 'cities'

    # Primary key for the City table
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)

    # Name of the city
    name = Column(String(128), nullable=False)

    # Foreign key to the state table
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)

    # Relationship with the State class.
    # CASCADE on delete and update.
    state = relationship("State",
                         back_populates="cities",
                         ondelete="CASCADE",
                         onupdate="CASCADE")

