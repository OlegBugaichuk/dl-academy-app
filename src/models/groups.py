from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from src.db.base import Base

groups_students = Table('groups_students',
                        Base.metadata,
                        Column('student_id', ForeignKey('users.id')),
                        Column('group_id', ForeignKey('groups.id')))


class Group(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    number = Column(String(5))

    lector_id = Column(Integer, ForeignKey('users.id'))
    lector = relationship('User', backref='lector_groups')

    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship('Course', backref='groups')

    students = relationship('User',
                            secondary='groups_students',
                            backref='groups')
