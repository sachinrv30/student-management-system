# Student Management System (Django)

This is a Django-based web application for managing students.

## Features
- Student registration
- Login & Logout
- Dashboard
- Add / Edit students
- Course listing

## Setup Instructions

1. Clone the repository:
git clone https://github.com/sachinrv30/student-management-system.git

2. Navigate to project:
cd student-management-system

3. Create virtual environment:
python3 -m venv venv
source venv/bin/activate

4. Install dependencies:
pip install -r requirements.txt

5. Run migrations:
python3 manage.py migrate

6. Start server:
python3 manage.py runserver

7. Open in browser:
http://127.0.0.1:8000/