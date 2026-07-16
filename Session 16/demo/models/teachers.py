from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# id, name, age, classroom_id
class TeacherModel(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    age = Column(Integer)
    classroom_id = Column(Integer, ForeignKey("classes.id"), unique=True)
    
    classroom = relationship(
        "ClassroomModel",
        back_populates="teacher",
        uselist=False
    )
    
    