'''importing sqlalchemy, sys and model_state'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
    
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))

Session = sessionmaker(bind=engine)
session = Session()

for state in session.query(State).filter(
            State.name.contains('a')).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
session.close()