from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.student_subject import student_subject

# id, name
class SubjectModel(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    
    # student_subjects = relationship(
    #     "StudentSubjectModel",
    #     back_populates="subject"
    # )
    
    students = relationship(
        "StudentModel",
        secondary=student_subject,
        back_populates="subjects"
    )