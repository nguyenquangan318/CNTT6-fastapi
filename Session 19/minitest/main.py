from fastapi import FastAPI
from database import Base, engine
from models.classrooms import ClassroomModel
from models.students import StudentModel
from routers.students import router as student_router

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(student_router)