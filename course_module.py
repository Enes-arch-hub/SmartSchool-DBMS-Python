def create_course_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            capacity INTEGER
        )
    """)
    conn.commit()


def add_course(conn, name, capacity):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO courses (name, capacity) VALUES (?, ?)",
        (name, capacity)
    )
    conn.commit()
    print("✅ Course added!")


def view_courses(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()

    print("\n📚 Courses List:")
    for row in rows:
        print(row)


def update_course(conn, course_id, name, capacity):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE courses
        SET name=?, capacity=?
        WHERE id=?
    """, (name, capacity, course_id))
    conn.commit()
    print("🔄 Course updated!")


def delete_course(conn, course_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE id=?", (course_id,))
    conn.commit()
    print("🗑️ Course deleted!")