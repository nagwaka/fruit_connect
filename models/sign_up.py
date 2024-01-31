#!/usr/bin/python3

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base import Base
# from product_type import user_product_association


class UserSignUp(Base):
    __tablename__ = 'user_signup'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone_number = Column(Integer)
    location = Column(String(100), nullable=False)
    # password_hash = Column(String(128), nullable=False)
    # profile_picture = Column(String(255)) # Store the file path or reference

    # profile_picture = relationship('ProfilePicture', back_populates='user')
    # product_types = relationship('ProductType', secondary=user_product_association, back_populates='users')
