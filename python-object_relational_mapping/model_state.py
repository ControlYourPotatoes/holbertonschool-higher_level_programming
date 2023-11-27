#!/usr/bin/python3
"""
Module to define the State class.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Creating declarative_base
Base = declarative_base()


class State(Base):
    """Defining State class mapped to states table in database hbtn_0e_6_usa.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
