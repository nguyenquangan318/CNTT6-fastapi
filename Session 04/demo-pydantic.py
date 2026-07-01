from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class CreateStudent(BaseModel):
    id:int
    name:str = Field(min_length=3, max_length=20)
    age: Optional[int] = 18

students = [
    {"id": 1, "name": "Nguyễn Văn A", "age":18},
    {"id": 2, "name": "Nguyễn Thị B", "age":19},
    {"id": 3, "name": "Trần Văn C", "age":20}
]

app = FastAPI()

# API có chức năng thêm 1 sinh viên mới
@app.post('/student')
def create_student(new_student: CreateStudent):
    return {
        "data": new_student
    }