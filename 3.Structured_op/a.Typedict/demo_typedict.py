from typing import TypedDict

class person(TypedDict):
    name:str
    age:int

new_p:person = {
    'name': 'namae',
    'age': 32
}

print(new_p)