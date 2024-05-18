#!/usr/bin/python3
"""
Contains ctate class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    Class with id and name attributes of each City
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), ForeignKey('states.id'))
