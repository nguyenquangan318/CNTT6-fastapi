# import
from fastapi import FastAPI

# Tạo thực thể
bai1 = FastAPI()

# Viết API
@bai1.get("/")
def get_root():
    return {
        "message": "Bai tap ve nha 1"
    }