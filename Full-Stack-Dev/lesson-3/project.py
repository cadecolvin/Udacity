from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect

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
    restaurants = session.query(Restaurant)
    return render_template('restaurants.html', restaurants=restaurants)

@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)

@app.route('/restaurants/<int:restaurant_id>/new', methods=['GET','POST'])
def create_menuitem(restaurant_id):
    if request.method == 'POST':
        new_item = MenuItem(name=request.form['name'],
                restaurant_id=restaurant_id)

        session.add(new_item)
        session.commit
        return redirect(url_for('restaurant_menu',
            restaurant_id=restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant_id=restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/<int:menuitem_id>/edit/',
            methods=['GET', 'POST'])
def edit_menuitem(restaurant_id, menuitem_id):
    if request.method == 'POST':
        item = session.query(MenuItem).filter_by(id=menuitem_id).one()
        item.name = request.form['name']
        session.add(item)
        session.commit()
        return redirect(url_for('restaurant_menu',
            restaurant_id=restaurant_id))
    else:
        return render_template('editMenuItem.html',
            restaurant_id=restaurant_id, menuitem_id=menuitem_id)

@app.route('/restaurants/<int:restaurant_id>/<int:menuitem_id>/delete/',
            methods=['GET','POST'])
def delete_menuitem(restaurant_id, menuitem_id):
    item = session.query(MenuItem).filter_by(id=menuitem_id).one()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('restaurant_menu',
            restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item=item)

if __name__ == '__main__':
    app.debug = True
    app.run()
