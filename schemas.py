from pydantic import BaseModel


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int


class UpdateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
