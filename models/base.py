#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import getenv


DB_USER = getenv('DB_USER', 'farmer')
DB_PASSWORD = getenv('DB_PASSWORD', '4711..tofarmeR')
DB_HOST = getenv('DB_HOST', 'localhost')
DB_NAME = getenv('DB_NAME', 'fruit_farmer')

# Create the database URL using the environment variables
DB_URL = 'mysql://{}:{}@{}/{}'.format(DB_USER,
                                      DB_PASSWORD,
                                      DB_HOST,
                                      DB_NAME)

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)
