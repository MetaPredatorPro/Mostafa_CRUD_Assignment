from flask import Flask, render_template, request, redirect, Response
from student import get_all_students, add_student, delete_student, update_student

# Initialize Flask app
app = Flask(__name__)

# Home route: displays all students
@app.route('/')
def index():
    students = get_all_students()
    return render_template('index.html', students=students)

# Add student: handles form submission
@app.route('/add', methods=['POST'])
def add():
    first = request.form['first_name']
    last = request.form['last_name']
    email = request.form['email']
    date = request.form['enrollment_date']
    add_student(first, last, email, date)
    return redirect('/')

# Delete student by ID
@app.route('/delete/<int:student_id>')
def delete(student_id):
    delete_student(student_id)
    return redirect('/')

# Edit student: loads form with existing data
@app.route('/edit/<int:student_id>')
def edit(student_id):
    students = get_all_students()
    student = next((s for s in students if s[0] == student_id), None)
    return render_template('edit.html', student=student)

# Update student: saves edited data
@app.route('/update/<int:student_id>', methods=['POST'])
def update(student_id):
    first = request.form['first_name']
    last = request.form['last_name']
    email = request.form['email']
    date = request.form['enrollment_date']
    update_student(student_id, first, last, email, date)
    return redirect('/')

# Search students by name or email
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    students = get_all_students()
    filtered = [s for s in students if query in s[1].lower() or query in s[2].lower() or query in s[3].lower()]
    return render_template('index.html', students=filtered, query=query)

# Export student list as CSV
@app.route('/export')
def export():
    students = get_all_students()
    csv_data = "ID,First Name,Last Name,Email,Enrollment Date\n"
    for s in students:
        csv_data += f"{s[0]},{s[1]},{s[2]},{s[3]},{s[4]}\n"
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=students.csv"}
    )

# Run the app
if __name__ == '__main__':
    app.run(debug=True)