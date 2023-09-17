#!/usr/bin/python3
"""
Description:
print the first state of a table
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_first_state():
    """
    Description: 
   
    Print the first element of a table
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)

    session_market = sessionmaker(bind=engine)
    with session_market() as session:
        states = session.query(State).first()

        if states is None or states == "":
            print("Nothing")
        else:
            print(f"{states.id}: {states.name}")


if __name__ == "__main__":
    print_first_state()
