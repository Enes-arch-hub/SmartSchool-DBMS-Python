import heapq

def get_top_students(conn):
    cursor = conn.cursor()

    # Create performance table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS performance (
            student_id INTEGER,
            score INTEGER
        )
    """)
    conn.commit()

    cursor.execute("SELECT student_id, score FROM performance")
    data = cursor.fetchall()

    # Use heap to get top students
    top_students = heapq.nlargest(3, data, key=lambda x: x[1])

    print("\n🏆 Top Students:")
    for student in top_students:
        print(f"Student ID: {student[0]}, Score: {student[1]}")


def add_performance(conn, student_id, score):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO performance (student_id, score) VALUES (?, ?)",
        (student_id, score)
    )
    conn.commit()
    print("📊 Performance added!")