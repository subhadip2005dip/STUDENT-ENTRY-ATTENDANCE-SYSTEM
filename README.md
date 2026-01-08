# 🏫 School Student & Attendance Management System

A full-stack **School Management System** built using **FastAPI** (backend) and **Vanilla JavaScript + HTML/CSS** (frontend).  
This project allows managing **students and attendance records** with a clean UI and RESTful APIs.

---

## ⚡ Features

### Student Management
- Add new students with ID, name, and class.
- Edit existing student details.
- Delete students.
- View all students or individual student details.

### Attendance Management
- Mark attendance for students (Present/Absent).
- Edit attendance records with date/time and class.
- Delete attendance records.
- View all attendance records.

### Others
- Real-time notifications (toast messages) for operations.
- Easy-to-use responsive UI.
- Fully functional **CRUD** operations.
- Cross-Origin support for frontend-backend communication.

---

## 🛠️ Technology Stack

| Layer        | Technology/Library |
|--------------|-----------------|
| Backend      | FastAPI, Pydantic, Python |
| Frontend     | HTML, CSS, JavaScript |
| Data Storage | JSON files (`students2.json`, `attendance2.json`) |
| Middleware   | CORS (Cross-Origin Resource Sharing) |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10+ installed
- Git installed
- A browser (Chrome/Edge/Firefox)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/your-username/school-management.git
cd school-management

Create a virtual environment (recommended)

python -m venv venv
# Activate on Windows
.\venv\Scripts\activate
# Activate on Linux/Mac
source venv/bin/activate


Install dependencies

pip install fastapi uvicorn pydantic


Run the FastAPI server

uvicorn main:app --reload


Open the frontend

Open index.html in your browser.

Make sure the BASE_URL in the JS matches your FastAPI server (http://127.0.0.1:8000).

📝 API Endpoints
Students
Method	Endpoint	Description
POST	/students/add	Add a new student
GET	/student/view	View all students
GET	/student/view/{id}	View student by ID
PUT	/student/edit/{id}	Edit student details
DELETE	/student/delete/{id}	Delete a student
Attendance
Method	Endpoint	Description
POST	/student/attendance/add	Mark student attendance
GET	/student/attendance/view	View all attendance records
PUT	/student/attendance/edit/{id}	Edit attendance record
DELETE	/student/attendance/delete/{id}	Delete attendance record

