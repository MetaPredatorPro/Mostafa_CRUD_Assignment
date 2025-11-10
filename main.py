from student import get_all_students, add_student

print("Welcome to Student Manager!")
print("Current students:")
for s in get_all_students():
    print(s)

print("\nAdd a new student:")
first = input("First name: ")
last = input("Last name: ")
email = input("Email: ")
date = input("Enrollment date (YYYY-MM-DD): ")

add_student(first, last, email, date)
print("Student added!")
