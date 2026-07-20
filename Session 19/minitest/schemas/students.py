from pydantic import BaseModel, ConfigDict

class ClassResponse(BaseModel):
    id: int
    class_code: str
    class_name: str
    model_config = ConfigDict(
        from_attributes=True
    )

class StudentResponse(BaseModel):
    id: int
    student_code: str
    full_name: str
    email: str
    classroom: ClassResponse
    model_config = ConfigDict(
        from_attributes=True
    )
    
class FullStudentResponse(BaseModel):
    status_code: int
    message: str
    data: list[StudentResponse]
    error: None
    path: str
    model_config = ConfigDict(
        from_attributes=True
    )
    
