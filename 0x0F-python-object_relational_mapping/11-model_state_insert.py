#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    query = session.query(State).filter(State.name == "Louisiana").first()
    print(query.id)