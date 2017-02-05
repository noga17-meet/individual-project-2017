from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from nogas_databases import Customer, Cats
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#You can add some starter data for your database
customer = Customer(name="noga", dob = 15, mob = 4 , yob = 2000 , email = "bynoga@walla.com" , phonenumber  = 052-7382419 , gender = "female")
session.add()
session.commit()

cats = Cats(name="moka", dob = 7, mob = 4 , yob = 2006 , info_about = "white fur, right eye green and left eye blue")
session.add()
session.commit()
