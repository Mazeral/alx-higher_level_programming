#!/usr/bin/python3
"""
    A script that prints all City objects from the database hbtn_0e_6_usa
    Username, password and dbname will be passed as arguments to the script.
"""


import sys

from relationship_state import Base, State
from relationship_city import City

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    """
    Main function that creates a session and adds a new state with a city to the database.
    Then it closes the session.

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

    # Create the tables
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session()

    # Create a new state object with a city
    state = State(name="California")
    # Add the new state to the session

    # Create a new city object
    city = City(name="San Francisco")
    # Add the new city to the session and add it to states
    state.cities.append(city)

    # Add the new state and city to the session
    session.add(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()


if __name__ == '__main__':
    main()
