def create_student_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT
        )
    """)
    conn.commit()


def add_student(conn, name, age, email):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
        (name, age, email)
    )
    conn.commit()
    print("✅ Student added!")


def view_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n📋 Students List:")
    for row in rows:
        print(row)


def update_student(conn, student_id, name, age, email):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET name=?, age=?, email=?
        WHERE id=?
    """, (name, age, email, student_id))
    conn.commit()
    print("🔄 Student updated!")


def delete_student(conn, student_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("🗑️ Student deleted!")