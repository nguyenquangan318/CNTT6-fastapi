from fastapi import FastAPI
from database import engine, Base
from routers.classrooms import router as classrooms_router
from models.students import StudentModel
from models.subjects import SubjectModel
from models.teachers import TeacherModel

Base.metadata.create_all(engine)

app = FastAPI()

@app.get('/')
def start():
    return {
        "message": "Server đang hoạt động"
    }

app.include_router(classrooms_router)


