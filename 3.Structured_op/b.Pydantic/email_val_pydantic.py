from pydantic import BaseModel, EmailStr
from typing import Optional


class Student(BaseModel):
    name: str = 'koyomi'
    age: Optional[int] = None
    email: EmailStr

new_student=  {'age': '32', 'email': 'python@xyz.com'}         # auto converts the neccessary str into int where necessary

student = Student(**new_student)
print(type(student))
print(student)