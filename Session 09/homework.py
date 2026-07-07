from fastapi import FastAPI, HTTPException, status, Request
from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

carriers = [
    {"id": 1, "code": "GHN", "name": "Giao Hang Nhanh", "max_weight_capacity": 5000, "status": "ACTIVE"},
    {"id": 2, "code": "GHTK", "name": "Giao Hang Tiet Kiem", "max_weight_capacity": 3000, "status": "ACTIVE"},
    {"id": 3, "code": "VTP", "name": "Viettel Post", "max_weight_capacity": 10000, "status": "SUSPENDED"}
]

app = FastAPI()

class CreateCarrier(BaseModel):
    id: int
    code: str
    name: str
    max_weight_capacity: int
    status: str
class BaseResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[Any]
    errors: Optional[Any]
    timestamp: str
    path: str

def create_response(req: Request, status_code: int, message: str, data = None, errors = None):
    return BaseResponse(
        status_code=status_code,
        message=message,
        data=data,
        errors=errors,
        timestamp=datetime.now().isoformat(),
        path=req.url.path
    )
    
@app.post('/carrier', status_code=status.HTTP_201_CREATED)
def create_post(new_carrier: CreateCarrier, request:Request):
    carrier = new_carrier.model_dump()
    carriers.append(carrier)
    return create_response(request, status.HTTP_200_OK, "Success!", carrier)
    
@app.get('/carriers')
def get_all_carrier(request:Request):
    return create_response(request, status.HTTP_200_OK, "Success!", carriers) 
    
@app.get('/carrier/{id}')
def get_carrie_by_id(id: int, request:Request):
    for c in carriers:
        if c['id'] == id:   
            return create_response(request, status.HTTP_200_OK, "Success!", c)
    raise HTTPException(status.HTTP_404_NOT_FOUND, "Dữ liệu không tồn tại")

@app.exception_handler(Exception)
def global_exception_handler(
    request: Request,
    exc: Exception
):
    response = create_response(request, status.HTTP_500_INTERNAL_SERVER_ERROR, "Failed!", errors=str(exc))
    return JSONResponse(
        content=response.model_dump(),
        status_code=response.status_code
    )

@app.exception_handler(RequestValidationError)
def global_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    response = create_response(request, status.HTTP_422_UNPROCESSABLE_CONTENT, "Failed!", errors=exc.errors())
    return JSONResponse(
        content=response.model_dump(),
        status_code=response.status_code
    )  
    
@app.exception_handler(HTTPException)
def global_exception_handler(
    request: Request,
    exc: HTTPException
):
    response = create_response(request, exc.status_code, "Failed!", errors=exc.detail)
    return JSONResponse(
        content=response.model_dump(),
        status_code=response.status_code
    )
