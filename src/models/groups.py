from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from src.db.base import Base

groups_students = Table('groups_students',
                        Base.metadata,
                        Column('student_id', ForeignKey('users.id')),
                        Column('group_id', ForeignKey('groups.id')))


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    number = Column(String(5))

    lector_id = Column(Integer, ForeignKey('users.id'))
    lector = relationship('User', back_populates='lector_groups')

    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship('Course', back_populates='groups')

    students = relationship('User',
                            secondary='groups_students',
                            back_populates='groups')
