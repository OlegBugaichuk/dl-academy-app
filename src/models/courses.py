from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.orm import relationship
from src.db.base import Base

courses_modules = Table('courses_modules',
                        Base.metadata,
                        Column('course_id', ForeignKey('courses.id')),
                        Column('module_id', ForeignKey('modules.id')))

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String(40))
    description = Column(String(50))
    
    groups = relationship('Group', backref='course')

    modules = relationship('Module',
                           secondary='courses_modules',
                           backref='courses')


class Module(Base):
    __tablename__ = 'modules'
    id = Column(Integer, primary_key=True)
    title = Column(String(40))
    description = Column(String(50))
    price = Column(Float)
    
    courses = relationship('Course',
                           secondary='courses_modules',
                           backref='modules')

    lessons = relationship('Lesson', backref='module')


class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True)
    title = Column(String(40))
    description = Column(String(50))
    module_id = Column(Integer, ForeignKey('modules.id'))
    module = relationship('Module', backref='lessons')