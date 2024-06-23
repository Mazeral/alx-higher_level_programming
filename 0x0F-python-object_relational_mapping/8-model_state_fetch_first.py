#!/usr/bin/python3
"""
This script fetches all states from the database and prints them
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    # Create a session to interact with the database
    session = Session()

    # Fetch all states from the database and order them by id
    states = session.query(State).order_by(State.id).first()

    if states is None:
        print("Nothing")
    # Print each state
    else states:
        print("{}: {}".format(states.id, states.name))

    session.close()
