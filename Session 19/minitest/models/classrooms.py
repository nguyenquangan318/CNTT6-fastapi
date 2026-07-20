from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class ClassroomModel(Base):
    __tablename__ = "classrooms"
    id = Column(Integer, autoincrement=True, primary_key=True)
    class_code = Column(String(20))
    class_name = Column(String(20))
    
    students = relationship(
        "StudentModel",
        back_populates="classroom"
    )