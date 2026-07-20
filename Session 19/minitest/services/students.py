from sqlalchemy.orm import Session, joinedload
from models.students import StudentModel

def get_all_service(db: Session):
    list_students = db.query(StudentModel).options(
        joinedload(StudentModel.classroom)    
    ).all()
    return list_students