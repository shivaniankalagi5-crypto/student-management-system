from database import (create_tables, add_student, get_all_students,
                      search_student, update_grade, delete_student)
from models import Student

def print_menu():
    print("""
╔══════════════════════════════════╗
║   Student Management System      ║
╠══════════════════════════════════╣
║  1. Add new student               ║
║  2. View all students             ║
║  3. Search student by name        ║
║  4. Update student grade          ║
║  5. Delete student                ║
║  6. Exit                          ║
╚══════════════════════════════════╝""")

def view_all():
    rows = get_all_students()
    if not rows:
        print("\n  No students found.")
        return
    print(f"\n  {'ID':<5} {'Name':<20} {'Age':<5} {'Course':<20} {'Grade'}")
    print("  " + "-" * 60)
    for row in rows:
        print(f"  {row[0]:<5} {row[1]:<20} {row[2]:<5} {row[4]:<20} {row[5]}")

def main():
    create_tables()

    while True:
        print_menu()
        choice = input("  Enter your choice (1-6): ").strip()

        if choice == "1":
            name   = input("  Name   : ").strip()
            age    = int(input("  Age    : "))
            email  = input("  Email  : ").strip()
            course = input("  Course : ").strip()
            grade  = input("  Grade (or press Enter to skip): ").strip() or "N/A"
            add_student(name, age, email, course, grade)
            s = Student(name, age, email, course, grade)
            s.display()

        elif choice == "2":
            view_all()

        elif choice == "3":
            name = input("  Enter name to search: ").strip()
            rows = search_student(name)
            if rows:
                for row in rows:
                    s = Student(row[1], row[2], row[3], row[4], row[5])
                    s.display()
            else:
                print("\n  No student found.")

        elif choice == "4":
            student_id = int(input("  Enter student ID: "))
            new_grade  = input("  Enter new grade : ").strip()
            update_grade(student_id, new_grade)

        elif choice == "5":
            student_id = int(input("  Enter student ID to delete: "))
            confirm = input("  Are you sure? (yes/no): ").strip().lower()
            if confirm == "yes":
                delete_student(student_id)

        elif choice == "6":
            print("\n  Goodbye!\n")
            break

        else:
            print("\n  Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()