from sqlalchemy import Column, Integer, String

from src.db.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(30))
    phone  = Column(String(12))
    email  = Column(String(50))
    patronomyc  = Column(String(30))
    type  = Column(String)
