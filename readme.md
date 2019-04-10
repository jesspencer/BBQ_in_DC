# Good-Grub

Menu application, where menu items listed can be updated by users. Database backed by SQLALchemy, (https://www.sqlalchemy.org/).

## DATABASE SETUP:
* 1. The Database has two tables or bases:
* 2. Table 1: Restaurant: which includes name of restaurant and id column (primary_key)
* 3. Table 2: Menuitem: which includes name, description, price, course (entree, appetizer, dessert), id (primary_key), restaurant_id (ForeignKey), restaurant  

## REQUIREMENTS
1. flask-sqlalchemy
2. python 2.7
3. flask
4. virtualenv
5. os
6. pip

## RUNNING DOCUMENTATION LOCALLY

##This project uses a virtual environment / The Setup
- Install Virtual Environment, (https://virtualenv.pypa.io/en/latest/installation/)
- Create the environment: virtualenv #nameofyourvirtualenv
- Install Python Version2.7: virtualenv -p/usr/bin/python2.7 #nameofyourvirtualenv
- Activate: source #nameofyourvirtualenv/bin/activate
- Deactivate: type 'deactivate' to end

## Flask Install

- Now Install Flask, type 'pip install Flask' (http://flask.pocoo.org/docs/1.0/installation/#)
- Now that flask is installed, install Flask-sqlalchemy, type 'pip install Flask-SQLALchemy' (https://pypi.org/project/Flask-SQLAlchemy/)

## Once virtual environment set, Flask and Flask-sqlalchemy loaded
* Clone the project: git clone https://github.com/jesspencer/good-grub.git
* cd good-Grub
* Create restaurantmenu.db, with 'python database_setup.py'
* Put some menus into the empty restaurant database, with 'python lotsofmenus.py'
* Start the flask application that will allow the menu to show in your browswer, with 'python project.py'
* Lastly, open the WebApp by typing the following into your browser, http://localhost:5000/restaurant/

## The program will list if any all the restaurants in your database and the following options:
 * create a new restaurant
 * see the menu
 * edit/delete the restaurant
 * edit/delete the menu item
* Interacting with these options will update the database.

## BUGS AND FEATURE REQUESTS
Have a bug or a feature request? Please open an [issue](https://github.com/jesspencer/good-grub/issues/new).

## DOCUMENTATION
This Restaurant-Menu-WebApp documentation included in this repo in the root directory is built with Python virtual database server, Flask web framework, and SQLAlchemy.  The docs may also be run locally in your Linux database server, or Linux version 2.7.9.

## CREATOR
**Jessica Spencer**
- github.com/jesspencer
- twitter.com/js13142
- linkedin.com/in/spenje/
