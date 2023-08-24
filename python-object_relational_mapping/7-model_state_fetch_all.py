#!/usr/bin/python3
"""
Script that lists all State objects from the database - Using module SQLAlchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State 

if __name__ == "__main__":

    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]), 
                            pool_pre_ping=True)       
        
    #create a session factory
    session = sessionmaker(bind=engine)

    #create a session object
    session = session()

    #Retrieve all states from the database and print their IDs and names
    for state in session.query(State). order_by(State.id):
        print("{}: {}".format(state.id, state.name))
