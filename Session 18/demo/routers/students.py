from fastapi import APIRouter ,Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.students import CreateStudent
from services.students import (
    get_all_students_service,
    create_student_service,
    update_student_service,
    add_subjects_service
)

router = APIRouter(prefix="/students", tags=['Students'])

@router.get('')
def get_all_student(db: Session = Depends(get_db)):
    list_students = get_all_students_service(db)
    return list_students

@router.post('')
def create_student(new_student: CreateStudent, db: Session = Depends(get_db)):
    student = create_student_service(db, new_student)
    if student is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Lớp học không tồn tại")
    return student

@router.put('/{id}')
def update_student(id: int, update_student: CreateStudent, db: Session = Depends(get_db)):
    student = update_student_service(db, id, update_student)
    if student == "Sinh viên không tồn tại":
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Sinh viên không tồn tại")
    if student == "Lớp học không tồn tại":
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Lớp học không tồn tại")
    return student

@router.put('/{id}/classrooms')
def add_subjects(id: int, subjects: list[int], db: Session = Depends(get_db)):
    student = add_subjects_service(db, id, subjects)
    return student