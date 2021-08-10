from sqlalchemy.orm import declarative_base
import sqlalchemy as db
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    