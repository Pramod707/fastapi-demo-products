from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

base = declarative_base()


class Products(base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
