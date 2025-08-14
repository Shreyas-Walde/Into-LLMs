from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name: str = 'koyomi'
    age: Optional[int] = None
    email: EmailStr 
    cgpa: float = Field(gt=0, lt =10, default=5, description= "A decimal value represents cgpa")   # setting deafult value

new_student=  {'age': '32', 'email': 'python@xyz.com'}         # auto converts the neccessary str into int where necessary

student = Student(**new_student)
student_dict = dict(student)  # stored in dict

print(student_dict['age'])


student_json = student.model_dump_json()   # stored in json
print(student_json)