from sqlalchemy.orm import Session, joinedload
from models.classrooms import ClassroomModel
from schemas.classrooms import CreateClassroom, UpdateClassroom

def get_all_classrooms_service(db: Session):
    list_classes = db.query(ClassroomModel).options(
        joinedload(ClassroomModel.students),
        joinedload(ClassroomModel.teacher)
    ).all()
    return list_classes

def get_class_by_id_service(db: Session, id: int):
    classroom = db.query(ClassroomModel).filter(ClassroomModel.id == id).options(
        joinedload(ClassroomModel.students),
        joinedload(ClassroomModel.teacher)
    ).first()
    return classroom

def create_class_services(db: Session, new_class: CreateClassroom):
    classroom = ClassroomModel(**new_class.model_dump())
    db.add(classroom)
    db.commit()
    db.refresh(classroom)
    return classroom

def delete_class_service(db: Session, id: int):
    classroom = db.query(ClassroomModel).filter(ClassroomModel.id == id).first()
    if classroom is None:
        return classroom
    db.delete(classroom)
    db.commit()
    return classroom

def update_class_service(db: Session, id: int, update_classroom: UpdateClassroom):
    classroom = db.query(ClassroomModel).filter(ClassroomModel.id == id).first()
    if classroom is None:
        return classroom
    for key, value in update_classroom.model_dump().items():
        setattr(classroom, key, value )
    db.commit()
    db.refresh(classroom)
    return classroom