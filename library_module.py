def create_library_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS library (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_name TEXT,
            student_id INTEGER,
            status TEXT
        )
    """)
    conn.commit()


def borrow_book(conn, book_name, student_id):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO library (book_name, student_id, status) VALUES (?, ?, ?)",
        (book_name, student_id, "Borrowed")
    )
    conn.commit()
    print("📖 Book borrowed!")


def return_book(conn, book_id):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE library
        SET status='Returned'
        WHERE id=?
    """, (book_id,))
    conn.commit()
    print("📚 Book returned!")


def view_books(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM library")
    rows = cursor.fetchall()

    print("\n📚 Library Records:")
    for row in rows:
        print(row)