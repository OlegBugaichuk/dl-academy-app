from pydantic import BaseModel


class GroupBase(BaseModel):
    number: str


class GoupNew(GroupBase):
    course_id: int
    lector_id: int


class Group(GroupBase):
    id: int

    class Config:
        orm_mode = True