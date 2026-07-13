from sqlalchemy.orm import Session
from schemas import CreateTeam
from models import TeamModel

def create_team_service(db: Session, new_team: CreateTeam):
    team = TeamModel(**new_team.model_dump())
    db.add(team)
    db.commit()
    db.refresh(team)
    return team

def get_all_service(db: Session):
    list_teams = db.query(TeamModel).all()
    return list_teams

def get_team_service(db: Session, id: int):
    team = db.query(TeamModel).filter(TeamModel.id == id).first()
    return team

def update_team_service(db: Session, id: int, update_team: CreateTeam):
    team = db.query(TeamModel).filter(TeamModel.id == id).first()
    if team is None:
        return team
    for key, value in update_team.model_dump().items():
        setattr(team, key, value)
    db.commit()
    db.refresh(team)
    return team

def delete_team_service(db: Session, id: int):
    team = db.query(TeamModel).filter(TeamModel.id == id).first()
    if team is None:
        return team
    db.delete(team)
    db.commit
    return team

def search_team_service(db: Session, group_name: str):
    list_teams = db.query(TeamModel).filter(TeamModel.group_name.like(f'%{group_name}%')).all()
    return list_teams