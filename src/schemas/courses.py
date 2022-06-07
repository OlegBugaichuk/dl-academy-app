from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    description: str = ""


class ModuleBase(BaseModel):
    title: str
    description: str = ""


class LessonBase(BaseModel):
    title: int
    description: int = ""


class LessonNew(LessonBase):
    module_id: int


class ModuleNew(ModuleBase):
    course_id: int


class CourseNew(CourseBase):
    pass


class Lesson(LessonBase):
    id: int

    class Config:
        orm_mode = True


class LessonDetail(Lesson):
    content: str


class Module(ModuleBase):
    id: int
    lessons: list[Lesson]

    class Config:
        orm_mode = True


class Course(CourseBase):
    id: int
    modules: list[Module]

    class Config:
        orm_mode = True
