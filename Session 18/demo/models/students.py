from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.student_subject import student_subject

# id, name, age, classroom_id
class StudentModel(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    age = Column(Integer)
    classroom_id = Column(Integer, ForeignKey("classes.id", ondelete="set null"))
    
    classroom = relationship(
        "ClassroomModel",
        back_populates="students",
        uselist=False
    )

    # student_subjects = relationship(
    #     "StudentSubjectModel",
    #     back_populates="student"
    # )
    
    subjects = relationship(
        "SubjectModel",
        secondary=student_subject,
        back_populates="students"
    )
    