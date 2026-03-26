import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect("school.db")
        print("✅ Connected to database")
        return conn
    except Exception as e:
        print("❌ Connection error:", e)