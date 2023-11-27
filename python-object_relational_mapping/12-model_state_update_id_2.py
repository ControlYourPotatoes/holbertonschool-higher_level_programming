#!/usr/bin/python3
"""
Changes the name of state
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    databases = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, databases))

    Session = sessionmaker(bind=engine)
    session = Session()

    state_update = session.query(State).filter(State.id == 2).first()
    state_update.name = 'New Mexico'
    session.commit()
