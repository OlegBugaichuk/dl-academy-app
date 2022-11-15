from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship
from src.db.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), default="")
    last_name = Column(String(30), default="")
    phone = Column(String(12), default="")
    email = Column(String(50))
    patronomyc = Column(String(30), default="")
    type = Column(String(10), default="student")
    password = Column(String(100))
    active = Column(Boolean, default=False)

    mentor_id = Column(Integer, ForeignKey('users.id'))
    students = relationship('User',
                            backref=backref('mentor', remote_side=[id]))

    lector_groups = relationship('Group', back_populates='lector')

    groups = relationship('Group',
                          secondary='groups_students',
                          back_populates='students')
