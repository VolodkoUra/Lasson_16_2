from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
"""
country
region
city
streets
"""

Base = declarative_base()



class Country(Base):
    __tablename__ = 'country'
    id = Column (Integer)
    name = Column(String)

class Region(Base):
    __tablename__ = 'region'
    id = Column (Integer)
    name = Column(String)
    id_country = Column(Integer, ForeignKey=Country.id)


