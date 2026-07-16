from fastapi import APIRouter ,Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.classrooms import CreateClassroom, UpdateClassroom, FullClassResponse
from services.classrooms import (
    get_all_classrooms_service,
    get_class_by_id_service,
    create_class_services,
    delete_class_service,
    update_class_service
)

router = APIRouter(prefix="/classrooms", tags=['Classrooms'])

@router.get('', response_model=list[FullClassResponse])
def get_all_classrooms(db: Session = Depends(get_db)):
    list_classes = get_all_classrooms_service(db)
    return list_classes
    
@router.get('/{id}', response_model=FullClassResponse)
def get_classroom_by_id(id: int, db: Session = Depends(get_db)):
    classroom = get_class_by_id_service(db, id)
    return classroom

@router.post("")
def create_classroom(new_classroom: CreateClassroom, db: Session = Depends(get_db)):
    classroom = create_class_services(db, new_classroom)
    return {
        "message": "Success!",
        "data": classroom
    }
    
@router.delete("/{id}")
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
    
@router.put("/{id}")
def update_classroom(id: int, update_classroom: UpdateClassroom, db: Session = Depends(get_db)):
    classroom = update_class_service(db, id, update_classroom)
    return {
        "message": "Success!",
        "data": classroom
    }