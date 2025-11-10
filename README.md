# Student CRUD Web App

This is a full-stack web application built with Python, Flask, and PostgreSQL that allows users to manage student records. It supports creating, reading, updating, deleting, searching, and exporting student data.

---

# Setup Instructions

1. Download the project folder.
2. Open a terminal and navigate to the project directory.
3. Create a virtual environment:
python -m venv venv
4. Activate the virtual environment:
- Windows:
  ```
  venv\Scripts\activate
  ```
5. Install required packages:
pip install flask psycopg2
6. Set up your PostgreSQL database and update `db.py` with your credentials.
7. Run the app:
python app.py
8. Open your browser and go to:
http://127.0.0.1:5000

---

# File Overview

- `app.py`: Main Flask application with all routes
- `db.py`: Handles database connection
- `student.py`: Contains all CRUD functions
- `test.py`: Script to test CRUD functions from the command line
- `templates/index.html`: Main page for viewing, adding, searching students
- `templates/edit.html`: Page for editing student info
- `static/style.css`: Styling for the web interface

---

# Function Explanations

`get_all_students()`
Fetches all student records from the database.

`add_student(first, last, email, date)`
Adds a new student with the given details.

`delete_student(student_id)`
Deletes a student by their ID.

`update_student(student_id, first, last, email, date)`
Updates an existing student's information.

# Video Demonstration
Watch the full video here: https://youtu.be/q0mrJxVyvfU

# Functions Implemented
- `get_all_students()`
- `add_student(...)`
- `update_student_email(...)`
- `delete_student(...)`

# Setup Instructions
1. Create PostgreSQL database `student_db`
2. Create `students` table using provided schema
3. Insert initial data
4. Run `python app.py` to launch the web app
5. Run `python test.py` to test backend functions

