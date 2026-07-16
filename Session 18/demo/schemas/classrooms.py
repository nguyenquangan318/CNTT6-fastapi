from pydantic import BaseModel, ConfigDict
from datetime import datetime

class CreateClassroom(BaseModel):
    class_code: str
    name: str
    description: str
    created_at: datetime
    
class UpdateClassroom(BaseModel):
    class_code: str
    name: str
    description: str
    
class StudentResponseInClass(BaseModel):
    id: int
    name: str
    age: int
    model_config = ConfigDict(
        from_attributes=True
    )
    
class TeacherResponseInClass(BaseModel):
    id: int
    name: str
    age: int
    model_config = ConfigDict(
        from_attributes=True
    )
    
class FullClassResponse(BaseModel):
    id: int
    class_code: str
    name: str
    description: str
    created_at: datetime
    students: list[StudentResponseInClass]
    teacher: TeacherResponseInClass
    model_config = ConfigDict(
        from_attributes=True
    )