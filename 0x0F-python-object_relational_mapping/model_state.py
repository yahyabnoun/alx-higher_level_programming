#!/usr/bin/python3
"""  lFirst state model """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
if __name__ == "__main__":

    class State(Base):
        __tablename__ = 'States'
        id = Column(Integer, primary_key=True,nullable=False, unique=True)
        name =  Column(String(128),nullable=False)
