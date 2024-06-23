#!/usr/bin/python3

"""
Script that fetches the first state
from the database that matches a given name
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """
    Main function that fetches the first state
    from the database that matches a given name
    """

    # Create a database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)

    # Create a session to interact with the database
    session = Session()

    # Fetch the first state from the database
    # that matches a given name and order them by id
    states = session.query(State).filter(
        State.name.like(sys.argv[4])).order_by(State.id).first()

    # If no states are found, print "Nothing"
    if states is None:
        print("Not found")
    # Otherwise, print the id and name of the first state
    else:
        print(states.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
