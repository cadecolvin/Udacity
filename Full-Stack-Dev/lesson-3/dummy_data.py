from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_restaurants(session):
    for idx in range(10):
        restaurant = Restaurant(name=f'Restaurant {idx}')
        session.add(restaurant)
        session = create_menu_items(session, restaurant)

    return session

def create_menu_items(session, restaurant):
    cheesepizza = MenuItem(name='Cheese Pizza', price='$8.99',
                           course='Entree', description='All Natural baby!',
                           restaurant=restaurant)
    session.add(cheesepizza)

    sausagepizza = MenuItem(name='Sausage Pizza', price='$9.99',
                           course='Entree', description='All Natural baby!',
                           restaurant=restaurant)
    session.add(sausagepizza)
    return session

session = create_restaurants(session)
session.commit()

restaurants = session.query(Restaurant).all()
for res in restaurants:
    print(res.name)
