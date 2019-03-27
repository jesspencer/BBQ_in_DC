from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

## Texas Jack's Bbq
restaurant1 = Restaurant(name="Texas Jack's Barbecue", stars= "4 stars")
session.add(restaurant1)
##staging field
session.commit()

menuItem1 = MenuItem(name = "Two-Door '87 Cutlass Supreme Nachos", description = "corn tortillas, queso, salsa verde, salsa roja, sour cream, cilantro and radishes", course = "Appetizer", price = "$6.00", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Four-Door '87 Cutlass Supreme Nachos", description = "corn tortillas, queso, salsa verde, salsa roja, sour cream, cilantro and radishes", course = "Appetizer", price = "$10.00", restaurant= restaurant1)
session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Wings", description ="crispy smoked wings, choice of buffalo sauce, barbecue sauce or old bay rubbed", course = "Appetizer", price = "$8.00", restaurant = restaurant1)
session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Tortilla Chips", description = "cripsy chips", course = "Appetizer", price = "$6.00", restaurant = restaurant1)
session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name= "Beef Short Rib", description = "weight of rib varies: 1.75lb - 2.5lb", course = "Entree", price = "$26.00", restaurant= restaurant1)
session.add(menuItem5)
session.commit()

menuItem7 = MenuItem(name= "Beef Brisket", description = "lean & moist", course = "Entee", price = "$12.00", restaurant= restaurant1)
session.add(menuItem7)
session.commit()

#KPOT Korean BBQ & Hot Pot

restaurant1 = Restaurant(name = "KPOT Korean BBQ & Hot Pot", stars = "3.5 stars")
session.add(restaurant1)
session.commit()

print "added items!"

print session.query(Restaurant).all
