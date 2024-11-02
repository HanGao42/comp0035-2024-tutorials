
import sqlite3
from pathlib import Path

# Define path for the database
music_db_path = Path(__file__).parent.joinpath("student_db_normalized.db").resolve()

# Connect to the SQLite database
connection = sqlite3.connect(music_db_path)
cursor = connection.cursor()

# Create tables
sql_create_students_table = """
CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    student_email TEXT UNIQUE NOT NULL
);
"""

sql_create_teachers_table = """
CREATE TABLE IF NOT EXISTS Teachers (
    teacher_id INTEGER PRIMARY KEY,
    teacher_name TEXT NOT NULL,
    teacher_email TEXT UNIQUE NOT NULL
);
"""

sql_create_courses_table = """
CREATE TABLE IF NOT EXISTS Courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    course_code TEXT UNIQUE NOT NULL,
    course_schedule TEXT,
    course_location TEXT
);
"""

sql_create_enrollment_table = """
CREATE TABLE IF NOT EXISTS Enrollment (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    teacher_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);
"""

# Execute table creation
cursor.execute(sql_create_students_table)
cursor.execute(sql_create_teachers_table)
cursor.execute(sql_create_courses_table)
cursor.execute(sql_create_enrollment_table)

# Insert sample data
sql_insert_student = "INSERT INTO Students (student_name, student_email) VALUES (?, ?);"
sql_insert_teacher = "INSERT INTO Teachers (teacher_name, teacher_email) VALUES (?, ?);"
sql_insert_course = "INSERT INTO Courses (course_name, course_code, course_schedule, course_location) VALUES (?, ?, ?, ?);"
sql_insert_enrollment = "INSERT INTO Enrollment (student_id, course_id, teacher_id) VALUES (?, ?, ?);"

students = [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com")
]
teachers = [
    ("Prof. John", "john@example.com"),
    ("Dr. Smith", "smith@example.com")
]
courses = [
    ("Mathematics", "MATH101", "Mon-Wed-Fri", "Room A"),
    ("Physics", "PHYS101", "Tue-Thu", "Room B")
]
enrollments = [
    (1, 1, 1),  # Alice enrolled in Mathematics taught by Prof. John
    (2, 2, 2)   # Bob enrolled in Physics taught by Dr. Smith
]

# Insert data into the tables
cursor.executemany(sql_insert_student, students)
cursor.executemany(sql_insert_teacher, teachers)
cursor.executemany(sql_insert_course, courses)
cursor.executemany(sql_insert_enrollment, enrollments)

# Commit and close
connection.commit()
connection.close()