from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db
from classroom_services import create_class_service, get_class_by_id_service, get_all_classes_service
from schemas import CreateClassroom

app = FastAPI()

@app.get('/test-connection')
def test_connect(db: Session = Depends(get_db)):
    try:
        db.execute(text('SELECT 1'))
        return {
            "messsage": "Success!"
        }
    except Exception as err:
        return {
            "message": str(err)
        }
        
@app.get('/classrooms')
def get_all_classes(db: Session = Depends(get_db)):
    list_classes = get_all_classes_service(db)
    return {
        "message": "Success!",
        "data": list_classes
    }
    
@app.get('/classrooms/{id}')
def get_class_by_id(id: int, db: Session = Depends(get_db)):
    classroom = get_class_by_id_service(id, db)
    if classroom is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Lop khong ton tai")
    return{
        "message": "Success!",
        "data": classroom
    }
    
@app.post('/classroom')
def create_class(new_class: CreateClassroom, db: Session = Depends(get_db)):
    classroom = create_class_service(new_class, db)
    return {
        "message": "Success!",
        "data": classroom
    }
        
