from sqlalchemy.orm import Session, joinedload
from models.students import StudentModel
from models.classrooms import ClassroomModel
from models.subjects import SubjectModel
from schemas.students import CreateStudent

def get_all_students_service(db: Session):
    list_students = db.query(StudentModel).options(
        joinedload(StudentModel.classroom)
    ).all()
    return list_students

def create_student_service(db: Session, new_student: CreateStudent):
    db_classroom = db.query(ClassroomModel).filter(ClassroomModel.id == new_student.classroom_id).first()
    if db_classroom is None:
        return None
    db_student = StudentModel(**new_student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student_service(db: Session, id: int, update_student: CreateStudent):
    db_student = db.query(StudentModel).filter(StudentModel.id == id).options(
        joinedload(StudentModel.classroom)
    ).first()
    if db_student is None:
        return "Sinh viên không tồn tại"
    db_classroom = db.query(ClassroomModel).filter(ClassroomModel.id == update_student.classroom_id).first()
    if db_classroom is None:
        return "Lớp học không tồn tại"
    for key, value in update_student.model_dump().items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student

def add_subjects_service(db: Session, id:int, subjects: list[int]):
    db_student = db.query(StudentModel).filter(StudentModel.id == id).options(
        joinedload(StudentModel.subjects)
    ).first()
    if db_student is None:
        return "Sinh viên không tồn tại"
    db_subjects = db.query(SubjectModel).filter(SubjectModel.id.in_(subjects)).all()
    db_student.subjects = db_subjects
    db.commit()
    db.refresh(db_student)
    return db_student