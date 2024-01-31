#!/usr/bin/python3

from sqlalchemy import Column, String, Integer
from base import Base

class UserSignIn(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=True)
    phone_number = Column(Integer, unique=True, nullable=True)
    password_hash = Column(String(128), nullable=False)

