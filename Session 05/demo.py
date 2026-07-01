from fastapi import FastAPI
from pydantic import BaseModel, Field

class CreateProduct(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0)

class UpdateProduct(BaseModel):
    name: str
    price: float

products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 300000},
    {"id": 3, "name": "Screen", "price": 400000}
]

app = FastAPI()

# Thao tác GET
# API lấy danh sách toàn bộ sản phẩm
@app.get('/products')
def get_product():
    return {
        "data": products
    }
    
# API lấy 1 sản phẩm theo id
@app.get('/product/{product_id}')
def get_product_by_id(product_id: int):
    for product in products:
        if product['id'] == product_id:
            return {
                "data": product
            }
    return {
        "data": None
    }
    
# API lấy danh sách sản phẩm theo khoảng giá
@app.get('/product')
def get_products_by_price(min: float, max:float):
    filter_products = []
    for product in products:
        if max >= product['price'] >= min:
            filter_products.append(product)
    if filter_products:
        return {
            "data": filter_products
        }
    return {
        "data": None
    }

# Thao tác POST
# API thêm sản phẩm mới
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
    
# Thao tác PUT
#  API cập nhật sản phẩm
@app.put('/product/{product_id}')
def update_product(product_id: int, update_product: UpdateProduct):
    for product in products:
        if product['id'] == product_id:
            product['name']= update_product.name
            product['price'] = update_product.price
            return {
                "message" : "Cập nhật thành công",
                "data": {
                    "id": product_id,
                    "name": update_product.name,
                    "price": update_product.price
                }
            }
    return {
        "message": "Không tìm thấy sản phẩm",
        "data": None
    }
    
# Thao tác DELETE
@app.delete('/product/{product_id}')
def delete_product(product_id: int):
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            return {
                "message": "Xóa thành công",
                "data": product
            }
    return {
        "message": "Không tìm thấy",
        "data": None
    }