from db import connect

# Fetch all student records from the database
def get_all_students():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    conn.close()
    return students

# Add a new student to the database
def add_student(first_name, last_name, email, enrollment_date):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
        (first_name, last_name, email, enrollment_date)
    )
    conn.commit()
    conn.close()

# Delete a student by ID
def delete_student(student_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    conn.close()

# Update an existing student's information
def update_student(student_id, first_name, last_name, email, enrollment_date):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE students SET first_name = %s, last_name = %s, email = %s, enrollment_date = %s WHERE id = %s",
        (first_name, last_name, email, enrollment_date, student_id)
    )
    conn.commit()
    conn.close()

# Update only the email of a student
def update_student_email(student_id, new_email):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE students SET email = %s WHERE student_id = %s",
        (new_email, student_id)
    )
    conn.commit()
    conn.close()
