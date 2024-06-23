#!/usr/bin/python3
"""
This script fetches all states from the database and prints them
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all states from the database and order them by id
    states = session.query(State).order_by(State.id).all()

    # Print each state
    for state in states:
        print("{}: {}".format(state.id, state.name))