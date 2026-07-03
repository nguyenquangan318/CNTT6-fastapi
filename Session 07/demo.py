from fastapi import FastAPI, status, Request, HTTPException
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Any
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse

products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 300000},
    {"id": 3, "name": "Screen", "price": 400000}
]

app = FastAPI()

class CreateProduct(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)

class BaseResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[Any]
    errors: Optional[Any]
    timestamp: str
    path: str
    
def create_response(req: Request, status_code: int, message: str, data = None, errors = None):
    return BaseResponse(
        status_code= status_code,
        message= message,
        data = data,
        errors = errors,
        timestamp= datetime.now().isoformat(),
        path = req.url.path
    )

@app.get('/products')
def get_all_products(request: Request):
    return create_response(request, status.HTTP_200_OK, "Success!", products)
    
@app.get('/product/{id}')
def get_product_by_id(request: Request, id: int):
    for p in products:
        if p['id'] == id:
            return create_response(request, status.HTTP_200_OK, "Success!", p)
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Dữ liệu không tồn tại")

@app.post('/product')
def create_product(new_product: CreateProduct):
    products.append({
        "id": new_product.id,
        "name": new_product.name,
        "price": new_product.price
    })
    return {
        "message": "Thêm mới thành công",
        "data": new_product
    }

@app.exception_handler(HTTPException)
def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    response = create_response(request, status.HTTP_404_NOT_FOUND, "Failed", errors = exc.detail)
    return JSONResponse(
        content = response.model_dump(),
        status_code = response.status_code
    )
    
@app.exception_handler(RequestValidationError)
def global_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    print(type(exc))
    response = create_response(request, status.HTTP_422_UNPROCESSABLE_CONTENT, "Failed", errors = exc.errors())
    return JSONResponse(
        content = response.model_dump(),
        status_code = status.HTTP_422_UNPROCESSABLE_CONTENT
    )
    
@app.exception_handler(Exception)
def global_exception_handler(
    request: Request,
    exc: Exception
):
    response = create_response(request, status.HTTP_500_INTERNAL_SERVER_ERROR, "Failed", errors = str(exc))
    return JSONResponse(
        content = response.model_dump(),
        status_code = response.status_code
    )
    
