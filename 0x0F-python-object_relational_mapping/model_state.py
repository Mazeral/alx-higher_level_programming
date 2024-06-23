#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Integer, String, Column, Table
from sqlalchemy.orm import sessionmaker
import sys

Base = declarative_base()


class State(Base):

    """
    Represents a state in the database.

    Attributes:
        id (int): The unique identifier of the state.
        name (str): The name of the state.
    """
    __tablename__ = "states"

    # The unique identifier of the state
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)

    # The name of the state
    name = Column(String(128),
                  nullable=False)
