def create_fee_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            amount REAL,
            status TEXT
        )
    """)
    conn.commit()


def add_fee(conn, student_id, amount, status):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO fees (student_id, amount, status) VALUES (?, ?, ?)",
        (student_id, amount, status)
    )
    conn.commit()
    print("💰 Fee record added!")


def view_fees(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fees")
    rows = cursor.fetchall()

    print("\n💳 Fee Records:")
    for row in rows:
        print(row)