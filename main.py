from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from datetime import datetime
import json
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Students(BaseModel):
    id :str
    name:str
    class_id:str

class Attendance(BaseModel):
     id:str
     date:str
     class_id:str
     status:str

def load_data():
     with open('students2.json','r')as f:
          return json.load(f)
     
def save_data(data):
     with open('students2.json','w')as f:
          return json.dump(data,f,indent=4,sort_keys=True)
     

def load_adata():
    with open('attendance2.json','r')as l:
          return json.load(l)
     
def save_adata(adata):
     with open('attendance2.json','w')as l:
         return json.dump(adata,l,indent=4,sort_keys=True)
     
     
@app.get("/")
def home_student():
     return{"message":"Student attandance and data portal"}
     
@app.post("/students/add")
def add_student(student:Students):
     data=load_data()
     if student.id in data:
        raise HTTPException(status_code=409, detail="Student already exists")
     data[student.id]=student.model_dump(exclude="id")
     save_data(data)
     return{"message":"Student added successfully"}

@app.get("/student/view")
def view_student(student:Students):
     data=load_data()
     return data

@app.get("/student/view/{id}")
def view_id(id:str):
     data=load_data()
     if  id in data:
          return data[id]
     raise HTTPException(status_code=404, detail="Student ID not found")

@app.post("/student/attendance/add")
def attendance_students(att: Attendance):
    adata = load_adata()   # now this is a DICT
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    adata[str(att.id)] = {
        "date": now,
        "class_id": att.class_id,
        "status": att.status,
    }

    save_adata(adata)
    return {"message": "Attendance Marked"}

@app.get("/student/attendance/view")
def view_student_attendance(attendance=Attendance):
     adata=load_adata()
     return adata

@app.put("/student/attendance/edit/{id}")
def edit_attendance_id(id: str, att: Attendance):
    adata = load_adata()

    if id not in adata:
        raise HTTPException(status_code=404, detail="Attendance record not found")

    adata[id] = {
        "date": att.date,
        "class_id": att.class_id,
        "status": att.status,
    }

    save_adata(adata)
    return {"message": "Attendance updated successfully"}

@app.delete("/student/attendance/delete/{id}")
def delete_attendance_id(id: str):
    adata = load_adata()

    if id not in adata:
        raise HTTPException(status_code=404, detail="Attendance record not found")

    del adata[id]
    save_adata(adata)

    return {"message": "Attendance deleted successfully"}

@app.put("/student/edit/{id}")
def edit_attendance(id: str, att: Students):
    data = load_data()

    if id not in data:
        raise HTTPException(status_code=404, detail="Attendance record not found")

    data[id] = {
         "name":att.name,
        "class_id": att.class_id,
    }

    save_data(data)
    return {"message": "Attendance updated successfully"}

@app.delete("/student/delete/{id}")
def delete_attendance_student(id: str):
    data = load_data()

    if id not in data:
        raise HTTPException(status_code=404, detail="Student record not found")

    del data[id]
    save_data(data)

    return {"message": "Student deleted successfully"}

     




     
     








    
