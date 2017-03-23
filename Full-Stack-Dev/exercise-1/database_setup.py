import sys

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import ForeignKey 
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import LargeBinary
from sqlalchemy import Numeric
from sqlalchemy import Date

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    city = Column(String(128))
    state = Column(String(2))
    zipCode = Column(String(10))
    address = Column(String(128))
    website = Column(String(256))

class Puppy(Base):
    __tablename__ = 'puppy'

    puppy_id = Column(Integer, primary_key=True)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    name = Column(String(128), nullable=False)
    dateOfBirth = Column(Date)
    gender = Column(String(6), nullable=False)
    weight = Column(Numeric(10))
    picture = Column(String)

    shelter = relationship(Shelter)


engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
