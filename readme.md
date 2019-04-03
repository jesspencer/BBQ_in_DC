# Good-Grub

Menu application, where menu items listed can be updated by users. Database backed by SQLALchemy, (https://www.sqlalchemy.org/).

## WHAT'S INCLUDED:
* 1. The Database has two tables or bases:
* 2. Table 1: Restaurant: which includes name of restaurant and id column (primary_key)
* 3. Table 2: Menuitem: which includes name, description, price, course (entree, appetizer, dessert), id (primary_key), restaurant_id (ForeignKey), restaurant  

## REQUIREMENTS
1. flask-sqlalchemy
2. python 2.7
3. flask
4. virtualenv
5. os

## HOW TO RUN
1. Install virtualenv: virtualenv #nameofyourvirtualenv
-- this creates the virtual environment

2. Choose which python version: virtualenv -p/usr/bin/python2.7 #nameofyourvirtualenv
-- this install python2.7

3. Activate: source #nameofyourvirtualenv/bin/activate
 -- this activates the environment -- type 'deactivate' to end

4. Install Flask
-- pip install Flask
5. Install Flask-sqlalchemy
-- pip install Flask-SQLALchemy

6. Clone the project: git clone https://github.com/jesspencer/good-grub.git

7. cd good-Grub
8. Run database_setup.py
--this creates restaurantmenu.db
9. Run lotsofmenus.py
--this provides the menus that will be in the database
10. Run project.py
--this is the flask application that will allow the menus to show in your web browser

## BUGS AND FEATURE REQUESTS
Have a bug or a feature request? Please open an [issue](https://github.com/jesspencer/good-grub/issues/new).

## DOCUMENTATION
This Restaurant-Menu-WebApp documentation included in this repo in the root directory is built with Python version 2.7.9, Flask web framework, and SQLAlchemy.  The docs may also be run locally in your Linux database server, or Linux virtual databaser server.


## RUNNING DOCUMENTATION LOCALLY
- 1. If necessary, install Python version 2.7.9, Flask web framework (http://flask.pocoo.org/docs/0.10/installation/), and SQLAlchemy (http://www.sqlalchemy.org/download.html) in a Linux database server or Linux virtual database server
- 2. From the root /Restaurant-Menu-WebApp directory, run database_setup.py in the command line by typing, "python database_setup.py"
- 3. From the root /Restaurant-Menu-WebApp directory, run finalproject.py in the command line by typing, "python finalproject.py"
- 4. Open your web browser using the link, http://localhost:5000/restaurant/
* The program will list if any all the restaurants in your database and the following options,
 * create a new restaurant
 * see the menu
 * edit/delete the restaurant
 * edit/delete the menu item
* Interacting with these options will update the database.


## CREATOR
**Jessica Spencer**
- github.com/jesspencer
- twitter.com/js13142
- linkedin.com/in/spenje/
