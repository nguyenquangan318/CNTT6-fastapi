from database import Base
from sqlalchemy import Column, Integer, String

class TeamModel(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String(20))
    coach_name = Column(String(20))
    group_name = Column(String(20))
    points = Column(Integer)