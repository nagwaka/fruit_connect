from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class ProfilePicture(Base):
    __tablename__ = 'profile_picture'

    id = Column(Integer, primary_key=True)
    filename = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship('UserSignUp', back_populates='profile_picture')

