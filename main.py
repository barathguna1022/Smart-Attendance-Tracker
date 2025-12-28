from student import add_student, list_students
from performance import add_performance, calculate_average


while True:
    print("!. Add student")
    print("2. List students")
    print("3. Mark attendance")
    print("4. view attendance")
    print("5. Add performance")
    print("6. View student report")
    print("7. Exit")
    choice = input("Enter your choice:")
    
    if choice == "1":
        add_student()

    elif choice == "2":
        list_students()

    elif choice == "5":
        add_performance()

    elif choice == "6":
        student_id = input("Enter Student ID: ")
        percentage, grade = calculate_average(student_id)

        if percentage is None:
            print("No performance data found.")
        else:
            print(f"Overall Percentage: {percentage:.2f}%")
            print(f"Grade: {grade}")
    elif choice == "7":
        print("Exiting program...")
    break

else:
    print("Invalid choice. Try again.")