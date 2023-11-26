#!/usr/bin/python3
"""
Module to define the City class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


# Creating declarative_base
Base = declarative_base()


class City(Base):
    """
    Defining City class mapped to cities table in database hbtn_0e_14_usa.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)