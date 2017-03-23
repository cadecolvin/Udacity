import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppyshelter.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_all_puppies(order_field):
    puppies = session.query(Puppy).order_by(order_field).all()
    return puppies

puppies_by_name = get_all_puppies(Puppy.name)
puppies_by_weight = get_all_puppies(Puppy.weight)

for puppy in puppies_by_name:
    print(puppy.name)

for puppy in puppies_by_weight:
    print(puppy.weight)


