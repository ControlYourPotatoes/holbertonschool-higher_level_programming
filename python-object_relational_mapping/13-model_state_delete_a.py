#!/usr/bin/python3
"""
Module to delete all State objects that contain the letter 'a' from database
hbtn_0e_6_usa.
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Function that deletes all State objects that contain the letter 'a' from
    database hbtn_0e_6_usa."""

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    my_session = Session()

    for state in my_session.query(State).filter(State.name.like('%a%')):
        my_session.delete(state)

    my_session.commit()

    my_session.close()
