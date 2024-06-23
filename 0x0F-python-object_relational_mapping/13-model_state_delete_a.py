#!/usr/bin/python3
"""
This script fetches all states from the database
that contain the letter 'a' in their name
and prints them.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """
    Main function that connects to the database,
    fetches states containing 'a' in their name,
    and prints them.

    Args:
        sys.argv[1]: username
        sys.argv[2]: password
        sys.argv[3]: database name
    """

    # Connect to the database
    # Format the connection string with the provided username,
    # password, and database name
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all states from the database that contain
    # the letter 'a' in their name
    # Order them by id
    delete_states = session.query(State).filter(
        State.name.contains("a")).order_by(State.id).all()

    # Delete the fetched states from the database
    for state in delete_states:
        session.delete(state)
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
