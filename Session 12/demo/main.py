from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas import CreateClassroom, UpdateClassroom
from models import Base
from database import engine
from services import (
    get_all_classrooms_service,
    get_class_by_id_service,
    create_class_services,
    delete_class_service,
    update_class_service
)
app = FastAPI()

Base.metadata.create_all(engine)

@app.get('/classrooms')
def get_all_classrooms(db: Session = Depends(get_db)):
    list_classes = get_all_classrooms_service(db)
    return {
        "message": "Success!",
        "data": list_classes
    }
    
@app.get('/classrooms/{id}')
def get_classroom_by_id(id: int, db: Session = Depends(get_db)):
    classroom = get_class_by_id_service(db, id)
    return {
        "mesage": "Success!",
        "data": classroom
    }
    
@app.post("/classrooms")
def create_classroom(new_classroom: CreateClassroom, db: Session = Depends(get_db)):
    classroom = create_class_services(db, new_classroom)
    return {
        "message": "Success!",
        "data": classroom
    }
    
@app.delete("/classrooms/{id}")
def delete_classroom(id: int, db: Session = Depends(get_db)):
    delete_classroom = delete_class_service(db, id)
    if delete_classroom is None:
       raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "Không tìm thấy lớp"
       ) 
    return {
        "message": "success!",
        "data": delete_classroom
    }
    
@app.put("/classrooms/{id}")
def update_classroom(id: int, update_classroom: UpdateClassroom, db: Session = Depends(get_db)):
    classroom = update_class_service(db, id, update_classroom)
    return {
        "message": "Success!",
        "data": classroom
    }