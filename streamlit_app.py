import streamlit as st
import sqlite3
import pandas as pd

# DB Connection
conn = sqlite3.connect("school.db", check_same_thread=False)

st.set_page_config(page_title="SMS Dashboard", layout="wide")

# LOGIN SYSTEM
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🔐 Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "1234":
            st.session_state.logged_in = True
        else:
            st.error("Invalid credentials")

if not st.session_state.logged_in:
    login()
    st.stop()

# DASHBOARD
st.title("🎓 School Management System")

menu = st.sidebar.selectbox("Menu", [
    "Students", "Courses", "Fees", "Library", "Analytics"
])

# STUDENTS
if menu == "Students":
    st.header("👨‍🎓 Students")

    name = st.text_input("Name")
    age = st.number_input("Age")
    email = st.text_input("Email")

    if st.button("Add Student"):
        conn.execute("INSERT INTO students (name, age, email) VALUES (?,?,?)",
                     (name, age, email))
        conn.commit()
        st.success("Student Added")

    df = pd.read_sql("SELECT * FROM students", conn)
    st.dataframe(df)

# COURSES
elif menu == "Courses":
    st.header("📚 Courses")

    cname = st.text_input("Course Name")
    cap = st.number_input("Capacity")

    if st.button("Add Course"):
        conn.execute("INSERT INTO courses (name, capacity) VALUES (?,?)",
                     (cname, cap))
        conn.commit()
        st.success("Course Added")

    df = pd.read_sql("SELECT * FROM courses", conn)
    st.dataframe(df)

# FEES
elif menu == "Fees":
    st.header("💰 Fees")

    sid = st.number_input("Student ID")
    amount = st.number_input("Amount")
    status = st.selectbox("Status", ["Paid", "Pending"])

    if st.button("Add Fee"):
        conn.execute("INSERT INTO fees (student_id, amount, status) VALUES (?,?,?)",
                     (sid, amount, status))
        conn.commit()
        st.success("Fee Added")

    df = pd.read_sql("SELECT * FROM fees", conn)
    st.dataframe(df)

# LIBRARY
elif menu == "Library":
    st.header("📖 Library")

    book = st.text_input("Book Name")
    sid = st.number_input("Student ID")

    if st.button("Borrow Book"):
        conn.execute("INSERT INTO library (book_name, student_id, status) VALUES (?,?,?)",
                     (book, sid, "Borrowed"))
        conn.commit()
        st.success("Book Borrowed")

    df = pd.read_sql("SELECT * FROM library", conn)
    st.dataframe(df)

# ANALYTICS (CHARTS 🔥)
elif menu == "Analytics":
    st.header("📊 Performance Analytics")

    sid = st.number_input("Student ID")
    score = st.number_input("Score")

    if st.button("Add Score"):
        conn.execute("INSERT INTO performance (student_id, score) VALUES (?,?)",
                     (sid, score))
        conn.commit()
        st.success("Score Added")

    df = pd.read_sql("SELECT * FROM performance", conn)

    if not df.empty:
        st.subheader("Top Performers")
        top = df.sort_values(by="score", ascending=False).head(5)
        st.bar_chart(top.set_index("student_id"))