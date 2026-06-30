# import
from fastapi import FastAPI

# Tạo thực thể
bai2 = FastAPI()

# Viết API
@bai2.get("/")
def get_root():
    return {
        "message": "Bai tap ve nha 2"
    }