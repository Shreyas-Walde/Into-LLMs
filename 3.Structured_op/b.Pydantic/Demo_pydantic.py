from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    name: str = 'koyomi'
    age: Optional[int] = None

new_student=  {'age': '32'}         # auto converts the neccessary str into int where necessary

student = Student(**new_student)
print(type(student))
print(student)