#!/usr/bin/python3

"""
Script that updates a state in the database given its id
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """
    Main function that updates a state in the database given its id

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
    Base.metadata.create_all(engine)
    # Create a session to interact with the database
    session = Session()

    # Query the state with id 2 and update its name
    update_obj = session.query(State).filter(State.id == 2).first()
    update_obj.name = 'New Mexico'
    session.commit()
    # Close the session
    session.close()


if __name__ == "__main__":
    main()
