#!/usr/bin/python3
"""
Module to add the State object "Louisiana" to the database hbtn_0e_6_usa.
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Function that adds the State object "Louisiana" to the database."""

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    my_session = Session()

    new_state = State(name="Louisiana")

    my_session.add(new_state)

    my_session.commit()

    print("{}".format(new_state.id))

    my_session.close()
