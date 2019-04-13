from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, make_response
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import *
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from login_decorator import login_required

# Flask
app = Flask(__name__)

#anti forgery imports
from flask import session as login_session
import os, random, string, datetime, json,httplib2, requests

#GCONNECT
CLIENT_ID = json.loads(
    open ('client_secrets.json', 'r'). read())['web']['client_id']
APPLICATION_NAME = "Restaurant App"


#DATABASE
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

#Creating An Anti-Forgery State Token
@app.route('/login')
def showLogin():
    state = ''.join(
        random.choice(string.ascii_uppercase + string.digits)for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE = state)

#GConnection
@app.route('/gconnect', methods = ['POST'])
def gconnect():

    #Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers ['content-type'] = 'application/json'
        return response

    #Obtain  authorization code also compatible with python3
    request.get_data()
    code = request.data.decode('utf-8')
    try:
        #upgrade the authorization code into a credential object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope = '')
        oauth_flow.redirect_uri = 'post message'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade teh authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    # Submit request, parse response - Python3 compatible
    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token Google plus ID is used for the intended user
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify the access toekn is valid for this application

    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's ."), 401)
        response.headers['Content-Type'] = 'application/json'
        return.response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')

    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'), 200)

        response.headers['Content-Type'] = 'application/json'
        return response

    #store the access token in the session for later use
    login_session['access_token'] = access_token
    login_session['gplus_id'] = gplus_id

    #Getting user information
    user_info_url= "https://www.googleapis.com/oauth2/v/user_info"
    params = {'acccess_token': access_token, 'alt':'json'}
    answer = requests.get(userinfo_url, params = params)

    data = answer.json()
    login_session =['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant=session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(id=restaurant_id).all()
    return jsonify(MenuItems = [i.serialize for i in items])

@app.route('/restaurant/<int:restaurant_id>menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    menuItem=session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem = menuItem.serialize)

@app.route('/restaurant/JSON')
def restaurantsJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify(restaurants=[r.serialize for r in restaurants])

@app.route('/')
@app.route('/restaurant/')
def showRestaurant():
    restaurants = session.query(Restaurant).order_by(asc(Restaurant.name))
    return render_template('restaurants.html', restaurants = restaurants)

# Create a new restaurant


@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'])
        session.add(newRestaurant)
        flash('New Restaurant %s Successfully Created' % newRestaurant.name)
        session.commit()
        return redirect(url_for('showRestaurant'))
    else:
        return render_template('newRestaurant.html')

# Edit a restaurant


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
            flash('Restaurant Successfully Edited %s' % editedRestaurant.name)
            return redirect(url_for('showRestaurant'))
    else:
        return render_template('editRestaurant.html', restaurant=editedRestaurant)


# Delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurantToDelete = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurantToDelete)
        flash('%s Successfully Deleted' % restaurantToDelete.name)
        session.commit()
        return redirect(url_for('showRestaurant', restaurant_id=restaurant_id))
    else:
        return render_template('deleteRestaurant.html', restaurant=restaurantToDelete)

# Show a restaurant menu

@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return render_template('menu.html', items=items, restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template(
        'menu.html', restaurant = restaurant, items=items, restaurant_id = restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/new', methods = ['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash('A new menu item was created!')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant_id = restaurant_id)

    return render_template('newMenuItem.html', restaurant=restaurant)


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/', methods = ['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method =='POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['name']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        session.add(editedItem)
        session.commit()
        flash("Menu item has been edited!")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('editMenuItem.html', restaurant_id=restaurant_id, menu_id=menu_id, item= editedItem)

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/', methods = ['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deletedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method =='POST':
        session.delete(deletedItem)
        session.commit()
        flash("Menu item has been deleted!")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item = deletedItem)

    return "page to delete a new menu item."

if __name__ =='__main__':
    app.debug = True
    app.secret_key = "super_secret_key"
    app.run(host='0.0.0.0', port = 5000, threaded = False)
