from fastapi import FastAPI

bai1 = FastAPI()

@bai1.get('/')
def get_root():
    return {
        "message":"Hello"
    }
    