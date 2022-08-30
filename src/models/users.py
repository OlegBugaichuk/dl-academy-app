from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref

from src.db.base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), default="")
    last_name = Column(String(30), default="")
    phone  = Column(String(12), default="")
    email  = Column(String(50))
    patronomyc  = Column(String(30), default="")
    type = Column(String(10), default="student")
    password = Column(String(100)) 
    active = Column(Boolean, default=False)

    mentor_id = Column(Integer, ForeignKey('users.id'))
    students = relationship('User',
                            backref=backref('mentor', remote_side=[id]))
