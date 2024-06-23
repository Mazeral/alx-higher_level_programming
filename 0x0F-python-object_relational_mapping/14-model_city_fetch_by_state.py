#!/usr/bin/python3
"""
This script fetches all states from the database and prints them,
along with their associated cities.
"""

import sys
from model_state import Base, City, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """
    Main function that fetches all states and their associated cities
    from the database and prints them.

    Args:
        sys.argv[1]: username
        sys.argv[2]: password
        sys.argv[3]: database name
    """

    # Create a database engine
    # Format the connection string with the provided username,
    # password, and database name
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all states from the database and order them by id
    states = session.query(State).order_by(State.id).all()

    # If no states are found, print "Nothing"
    if states is None:
        print("Nothing")
    # Print each state and its associated cities
    else:
        for state in states:
            for city in state.cities:
                print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    main()