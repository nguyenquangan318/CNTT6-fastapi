from fastapi import APIRouter, Depends, status, Request
from database import get_db
from sqlalchemy.orm import Session
from services.students import get_all_service
from schemas.students import FullStudentResponse
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/students", tags=["students"])

# def create_response():
#     return FullStudentResponse(
        
#     )

@router.get('', response_model=FullStudentResponse)
def get_all(request : Request, db:Session = Depends(get_db)):
    students = get_all_service(db)
    return FullStudentResponse(
        status_code=status.HTTP_200_OK,
        message="Lấy danh sách sinh viên thành công!",
        data= students,
        error=None,
        path=request.base_url.path
    )