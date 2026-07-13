from fastapi import FastAPI, Depends, status, HTTPException
from database import get_db, Base, engine
from sqlalchemy.orm import Session
from schemas import CreateTeam
from services import (
    create_team_service,
    get_all_service,
    get_team_service,
    update_team_service,
    delete_team_service,
    search_team_service
    )

app = FastAPI()

Base.metadata.create_all(engine)

@app.get('/')
def start():
    return {
        "message": "Server đang hoạt động"
    }
    
@app.post('/teams', status_code=status.HTTP_201_CREATED)
def create_team(new_team: CreateTeam, db: Session = Depends(get_db)):
    team = create_team_service(db, new_team)
    return {
        "data": team,
        "mesage": "Thêm đội thành công"
    }
    
@app.get('/teams')
def get_all_teams(db: Session = Depends(get_db)):
    list_teams = get_all_service(db)
    return {
        "data": list_teams,
        "message": "Lấy danh sách đội thành công"
    }

@app.get('/teams/search')
def search_team(group_name: str, db: Session = Depends(get_db)):
    list_teams = search_team_service(db, group_name)
    return {
        "data": list_teams,
        "message": "Tìm kiếm theo bảng đấu thành công"
    }

@app.get('/teams/{id}')
def get_team(id: int, db: Session = Depends(get_db)):
    team = get_team_service(db, id)
    if team is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Không tìm thấy đội")
    return {
        "data": team,
        "message": "Lấy đội theo id thành công"
    }
    
@app.put("/teams/{id}")
def update_team(id: int, update_team: CreateTeam, db: Session = Depends(get_db)):
    team = update_team_service(db, id, update_team)
    if team is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Không tìm thấy đội")
    return {
        "data": team,
        "message": "Cập nhật đội theo id thành công"
    }
    
@app.delete('/teams/{id}')
def delete_team(id: int, db: Session = Depends(get_db)):
    team = delete_team_service(db, id)
    if team is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Không tìm thấy đội")
    return {
        "data": team,
        "message": "Xóa đội theo id thành công"
    }
    

    