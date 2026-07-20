from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class StudentModel(Base):
    __tablename__ = "students"
    id = Column(Integer, autoincrement=True, primary_key=True)
    student_code = Column(String(20))
    full_name = Column(String(20))
    email = Column(String(20))
    class_id = Column(Integer, ForeignKey("classrooms.id"))
    
    classroom = relationship(
        "ClassroomModel",
        back_populates="students",
        uselist=False
    )