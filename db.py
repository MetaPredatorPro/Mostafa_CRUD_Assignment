import psycopg2

# Connects to the PostgreSQL database using the provided credentials
def connect():
    return psycopg2.connect(
        dbname="student_db",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )

