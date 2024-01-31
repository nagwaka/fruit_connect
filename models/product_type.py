from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from base import Base


user_product_association = Table('user_product_association',
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('product_type_id', Integer, ForeignKey('product_type.id'))
)

class ProductType(Base):
    __tablename__ = 'product_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    users = relationship('UserSignUp', secondary=user_product_association, back_populates='product_types')

