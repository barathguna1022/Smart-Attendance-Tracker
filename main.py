from student import add_student, list_students

while True:
    print("!. Add student")
    print("2. List students")
    print("3. Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        add_student()
    elif choice == "2":
        list_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")