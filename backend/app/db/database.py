from sqlalchemy import create_engine #create database conn between fast api and postgresql
from sqlalchemy.orm import sessionmaker,DeclarativeBase #create database sessions and DeclarativeBase is a base class of all database models will inherit from.

from app.core.config import settings #this is used for allowing access values from .env 

engine=create_engine(settings.DATABASE_URL)


