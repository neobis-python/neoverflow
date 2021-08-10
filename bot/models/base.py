import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from decouple import config


DATABASE_URI = config('DATABASE_URI')

engine = create_engine(DATABASE_URI, echo=True, future=True)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)