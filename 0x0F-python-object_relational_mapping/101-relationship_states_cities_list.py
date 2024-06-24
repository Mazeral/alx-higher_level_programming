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
    Main function that creates a session and prints all states and their cities.
    Username, password and dbname are passed as command line arguments.
    """

    # Create a database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)

    # Create the tables
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session()

    # Create a new state object with a city
    states = session.query(State).order_by(State.id).all()

    # Print all states and their cities
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id} {city.name}")

    # Commit the changes to the database
    session.commit()
    # Close the session
    session.close()


if __name__ == '__main__':
    main()
