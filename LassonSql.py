import sqlalchemy
from sqlalchemy.orm import sessionmaker


import models

engine = sqlalchemy.create_engine('sqlite:///TestDB.db', echo= True)
session = sessionmaker(bind= engine)



