#!/usr/bin/python3
"""
This script fetches the first state from the database and prints it.

Usage:
    python4 8-model_state_fetch_first.py <username> <password> <database_name>
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    # Create a database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3307/{}'
                           .format(sys.argv[2], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)

    # Create a session to interact with the database
    session = Session()

    # Fetch the first state from the database and order them by id
    states = session.query(State).order_by(State.id).first()

    # If no states are found, print "Nothing"
    if states is None:
        print("Nothing")
    # Otherwise, print the id and name of the first state
    else:
        print("{}: {}".format(states.id, states.name))

    # Close the session
    session.close()
