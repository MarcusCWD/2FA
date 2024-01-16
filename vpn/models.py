from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


### Declare all tables and relationships here below ###

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True)
    username = Column(String(length=30), nullable=False, unique=True)
    email_address = Column(String(length=50), nullable=False, unique=True)
    password = Column(String(length=60), nullable=False)
    budget = Column(Integer(), nullable=False, default=1000)
    items = relationship('Item', backref='owned_user', lazy=True)