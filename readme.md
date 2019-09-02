# Good-Grub
Interactive Restaurant WebApp, where the user has a landing page of menus.
The user is then able to update, delete, or add more menus to the Restaurant WebApp.  
Database used was SQLALchemy, (https://www.sqlalchemy.org/).

## Database Design:
* 1. The Database has two tables:
* 2. Table 1: Restaurant: which includes name of restaurant and id column (primary_key)
* 3. Table 2: Menuitem: which includes name, description, price, course (entree, appetizer, dessert), id (primary_key), restaurant_id (ForeignKey), restaurant  

## REQUIREMENTS
- flask-sqlalchemy
- python 3.7
- flask
- virtualenv
- os
- pip

## RUNNING DOCUMENTATION LOCALLY:
1. Create a VM; here are the steps [Creating_A_VM](https://github.com/jesspencer/Good-Grub/blob/master/Creating_A_VM.md)
2. Install Flask and Flask-SQLALchemy to your VM; here are the steps [Flask_Flask-SQLALchemy](https://github.com/jesspencer/Good-Grub/blob/master/Flask_Flask-SQLALchemy.md)
3. Run the virtual environment
4. Clone the project https://github.com/jesspencer/good-grub.git
5. cd good-Grub
6. Start the flask application that will allow the menu to show in your browswer, with `python finalproject.py`
7. Open the WebApp by pasting the following into your browser: http://localhost:5000/restaurant/

## Adding different menus
If you would like to replace the menus in this project with ones of your own Do It!
1. Delete the restaurantmenu.db file that you have cloned.
2. Create restaurantmenu.db, with `python database_setup.py`
4. Open the lotsofmenus.py file in your text editor and replace the restaurant names, menu item names, and save file.  
5. Put some menus into the empty restaurant database, with `python lotsofmenus.py`

## The application will list if any all the restaurants in your database and the following options:
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
