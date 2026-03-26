from db_connection import create_connection
from student_module import *
from course_module import *
from fee_module import *
from library_module import *
from analytics_module import *

def main():
    conn = create_connection()

    # Create all tables
    create_student_table(conn)
    create_course_table(conn)
    create_fee_table(conn)
    create_library_table(conn)

    while True:
        print("\n===== SCHOOL MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Course")
        print("6. View Courses")
        print("7. Update Course")
        print("8. Delete Course")
        print("9. Add Fee")
        print("10. View Fees")
        print("11. Borrow Book")
        print("12. Return Book")
        print("13. View Library")
        print("14. Add Performance")
        print("15. View Top Students")
        print("16. Exit")

        choice = input("Choose option: ")

        # STUDENTS
        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            email = input("Email: ")
            add_student(conn, name, age, email)

        elif choice == "2":
            view_students(conn)

        elif choice == "3":
            student_id = int(input("Student ID: "))
            name = input("New Name: ")
            age = int(input("New Age: "))
            email = input("New Email: ")
            update_student(conn, student_id, name, age, email)

        elif choice == "4":
            student_id = int(input("Student ID: "))
            delete_student(conn, student_id)

        # COURSES
        elif choice == "5":
            cname = input("Course Name: ")
            cap = int(input("Capacity: "))
            add_course(conn, cname, cap)

        elif choice == "6":
            view_courses(conn)

        elif choice == "7":
            course_id = int(input("Course ID: "))
            cname = input("New Course Name: ")
            cap = int(input("New Capacity: "))
            update_course(conn, course_id, cname, cap)

        elif choice == "8":
            course_id = int(input("Course ID: "))
            delete_course(conn, course_id)

        # FEES
        elif choice == "9":
            student_id = int(input("Student ID: "))
            amount = float(input("Amount: "))
            status = input("Status (Paid/Pending): ")
            add_fee(conn, student_id, amount, status)

        elif choice == "10":
            view_fees(conn)

        # LIBRARY
        elif choice == "11":
            book = input("Book Name: ")
            student_id = int(input("Student ID: "))
            borrow_book(conn, book, student_id)

        elif choice == "12":
            book_id = int(input("Book ID: "))
            return_book(conn, book_id)

        elif choice == "13":
            view_books(conn)

        # PERFORMANCE
        elif choice == "14":
            student_id = int(input("Student ID: "))
            score = int(input("Score: "))
            add_performance(conn, student_id, score)

        elif choice == "15":
            get_top_students(conn)

        # EXIT
        elif choice == "16":
            print("👋 Exiting system...")
            break

        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()