from pydantic import BaseModel


# Base class
class CourseBase(BaseModel):
    title: str
    description: str


# Course =====
class CourseNew(CourseBase):
    pass


class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True


# Module =====
class ModuleNew(CourseBase):
    price: float


class Module(ModuleNew):
    id: int

    class Config:
        orm_mode = True


# Lesson =====
class LessonNew(CourseBase):
    content: str
    module_id: int


class Lesson(LessonNew):
    id: int

    class Config:
        orm_mode = True


class LessonShort(CourseBase):
    id: int


# Rel schemas =====
class ModuleLessons(Module):
    lessons = list[LessonShort]


class CourseModules(Course):
    modules = list[ModuleLessons]