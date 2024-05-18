#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    querys = session.query(State.name, City.id, City.name).filter(
        City.state_id == State.id)
    for state_name, city_id, city_name in querys:
        print(f"{state_name}: ({city_id}) {city_name}")
