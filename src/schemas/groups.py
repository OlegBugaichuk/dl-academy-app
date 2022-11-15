from pydantic import BaseModel


class GroupBase(BaseModel):
    number: str
    lector_id: int
    course_id: int


class NewGroup(GroupBase):
    pass


class Group(GroupBase):
    id: int

    class Config:
        orm_mode = True
