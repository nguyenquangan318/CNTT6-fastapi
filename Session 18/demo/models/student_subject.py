from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

# id, student_id, subject_id
# Trường hợp bảng phụ có chức năng, thuộc tính riêng
# class StudentSubjectModel(Base):
#     __tablename__ = "student_subject"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     student_id = Column(Integer, ForeignKey("students.id"))
#     subject_id = Column(Integer, ForeignKey("subjects.id"))
    
#     student = relationship(
#         "StudentModel",
#         back_populates="student_subjects",
#         uselist=False
#     )
    
#     subject = relationship(
#         "SubjectModel",
#         back_populates="student_subjects",
#         uselist=False
#     )

# Trường hợp bảng chỉ có chức năng kết nối thôi
student_subject = Table(
    "student_subject",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("subject_id", Integer, ForeignKey("subjects.id"), primary_key=True)
)