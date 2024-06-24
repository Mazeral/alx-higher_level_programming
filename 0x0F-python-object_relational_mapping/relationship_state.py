#!/usr/bin/python3

"""
    this module contains a Base and State class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """
    State class inherits the Base class

    Attributes:
        id (int): Primary key for the state.
        name (string): Name of the state.
    """
    __tablename__ = 'states'

    # Define the columns of the table
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
