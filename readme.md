# Good-Grub

## Menu application, where menu items listed can be updated by users.

## The app will include:
1. Database backed by sqlalchemy, which uses sqlite:
2. The Database has two tables or bases
3. Table 1: Restaurant: which includes name of restaurant and id column (primary_key)
4. Table 2: Menuitem: which includes name, description, price, course (entree, appetizer, dessert), id (primary_key), restaurant_id (ForeignKey), restaurant  

## Requirements
1. flask-sqlalchemy
2. python 2.7
3. flask
4. virtualenv

## How to Run / Setup
1. Install virtualenv: virtualenv #nameofyourvirtualenv
-- this creates the virtual environment

2. Choose which python version: virtualenv -p/usr/bin/python2.7 #nameofyourvirtualenv
-- this install python2.7

3. Activate: source #nameofyourvirtualenv/bin/activate
 -- this activates the environment -- type 'deactivate' to end

4. Clone the project: git clone https://github.com/jesspencer/good-grub.git

4. cd good-Grub
5. Run database_setup.py
--this creates restaurantmenu.db
6. Run lotsofmenus.py
--this provides the menus that will be in the database
7. Run project.py
--this is the flask application that will allow the menus to show in your web browser
