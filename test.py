# Test script to demonstrate all CRUD operations

from student import add_student, get_all_students, update_student, delete_student

# Add a new student
add_student("Test", "User", "testuser@example.com", "2025-11-08")
print("Student added!")

# View all students
students = get_all_students()
print("All students:")
for s in students:
    print(s)

# Update the first student (if exists)
if students:
    student_id = students[0][0]
    update_student(student_id, "Updated", "User", "updated@example.com", "2025-11-09")
    print(f"Student {student_id} updated!")

# Delete the first student (if exists)
if students:
    delete_student(student_id)
    print(f"Student {student_id} deleted!")
