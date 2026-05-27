import sqlite3

DB_NAME = "students.db"

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT    NOT NULL,
            age     INTEGER NOT NULL,
            email   TEXT    UNIQUE NOT NULL,
            course  TEXT    NOT NULL,
            grade   TEXT
        )
    """)

    conn.commit()
    conn.close()

def add_student(name, age, email, course, grade="N/A"):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO students (name, age, email, course, grade)
            VALUES (?, ?, ?, ?, ?)
        """, (name, age, email, course, grade))
        conn.commit()
        print(f"\n  Student '{name}' added successfully!")
    except sqlite3.IntegrityError:
        print("\n  Error: Email already exists.")
    finally:
        conn.close()

def get_all_students():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_student(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM students
        WHERE name LIKE ?
    """, (f"%{name}%",))
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_grade(student_id, new_grade):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students SET grade = ?
        WHERE id = ?
    """, (new_grade, student_id))
    conn.commit()
    conn.close()
    print(f"\n  Grade updated successfully!")

def delete_student(student_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print(f"\n  Student deleted successfully!")