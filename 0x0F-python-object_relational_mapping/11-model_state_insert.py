#!/usr/bin/python3

"""
Script that inserts a new state into the database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """
    Main function that inserts a new state into the database

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

    # Create a session
    Session = sessionmaker(bind=engine)

    # Create a session to interact with the database
    session = Session()

    # Create a new state object
    new_state = State(name="Louisiana")
    # Add the new state to the session
    session.add(new_state)
    # Commit the changes to the database
    session.commit()
    # Close the session
    session.close()


if __name__ == "__main__":
    main()
