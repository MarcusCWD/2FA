from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


### Declare all tables and relationships here below ###

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True)
    email_address = Column(String(length=320), nullable=False, unique=True)
    epin = Column(String(3000), nullable=False)
    secret = Column(String(length=180), nullable=False)
    last_login = Column(Date(), nullable=True)
    # register_date = Column(Date(), nullable=False)
    active = Column(Boolean(), nullable=False, default=True)


class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer(), primary_key=True)
    email_address = Column(String(length=320), nullable=False, unique=True)
    password = Column(String(length=12), nullable=False)