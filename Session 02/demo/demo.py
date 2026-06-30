from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_root():
    return {
        "message":"Hello"
    }
    
@app.get('/goodbye')
def get_goodbye():
    return {
        "message":"Goodbye"
    }