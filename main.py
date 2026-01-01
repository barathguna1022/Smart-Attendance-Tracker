from student import add_student, list_students
from attendance import mark_attendance, view_attendance
from performance import add_performance, calculate_average

def pause():
    input("\nPress Enter to continue...")

while True:
    print("\n--- Smart Attendance & Performance Tracker ---")
    print("1. Add student")
    print("2. List students")
    print("3. Mark attendance")
    print("4. View attendance")
    print("5. Add performance")
    print("6. View student report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
        pause()

    elif choice == "2":
        list_students()
        pause()

    elif choice == "3":
        mark_attendance()
        pause()

    elif choice == "4":
        view_attendance()
        pause()

    elif choice == "5":
        add_performance()
        pause()

    elif choice == "6":
        student_id = input("Enter Student ID: ")
        percentage = calculate_average(student_id)

        if percentage is None:
            print("No performance records found for this student.")
        else:
            print(f"Average Performance: {percentage:.2f}%")

        pause()

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
