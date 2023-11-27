#!/usr/bin/python3
"""
Displays state requested
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    databases = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, databases))

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == state_name).first()

    if not state:
        print("Not found")

    else:
        print("{}".format(state.id))