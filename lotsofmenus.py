from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

restaurant1 = Restaurant(name="Texas Jack's Barbecue", stars= "4 stars")
session.add(restaurant1)
##staging field
session.commit()

menuItem1 = MenuItem(name = "Two-Door '87 Cutlass Supreme Nachos", description = "corn tortillas, queso, salsa verde, salsa roja, sour cream, cilantro and radishes", course = "Appetizer", price = "$6.00", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

print "added items!"

print session.query(Restaurant).all
