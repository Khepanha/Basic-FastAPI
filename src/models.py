from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(String, nullable = True)
    password = Column(String, nullable = True)
