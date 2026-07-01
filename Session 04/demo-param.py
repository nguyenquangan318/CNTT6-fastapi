from fastapi import FastAPI

students = [
    {"id": 1, "name": "Nguyễn Văn A", "age":18},
    {"id": 2, "name": "Nguyễn Thị B", "age":19},
    {"id": 3, "name": "Trần Văn C", "age":20}
]

app = FastAPI()

# Viết API có chức năng lấy toàn bộ sinh viên
@app.get('/students')
def get_students():
    return {
        "message": "Danh sách tất cả sinh viên",
        "data": students
    }

# Viết API có chức năng lấy 1 sinh viên theo id
# /student/1
@app.get("/student/{student_id}")
def get_student_by_id(student_id: int):
    for student in students:
        if student['id'] == student_id: 
            return {
                "data": student
            }
    return {
        "data": None
    }
    
# Viết API có chức năng lấy danh sách sinh viên trong khoảng tuổi
# /students?start_age=18&end_age=20
@app.get('/student')
def get_students_by_age(start_age: int, end_age: int):
    filter_students = []
    for student in students:
        if start_age <= student['age'] <= end_age:
            filter_students.append(student)
    if filter_students:
        return{
            "data":{
                "data": filter_students
            }
        }
    return {
        "data": None
    }