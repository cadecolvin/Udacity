from flask import Flask
from flask import render_template
from flask import url_for

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/')
def restaurants():
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)

@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)

@app.route('/restaurant/')
def create_menuitem():
    return 'Normally, you\'d add a restaurant here.'

@app.route('/restaurants/<int:restaurant_id>/<int:menuitem_id>/edit/')
def edit_menuitem(restaurant_id, menuitem_id):
    return 'Normally, you\'d edit a restaurant here.'

@app.route('/restaurants/<int:restaurant_id>/<int:menuitem_id>/delete/')
def delete_menuitem(restaurant_id, menuitem_id):
    return 'Normally, you\'d delete a restaurant here.'

if __name__ == '__main__':
    app.debug = True
    app.run()
