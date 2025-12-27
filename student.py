import csv
import os

FILE_PATH = "data/students.csv"

def add_student():
    student_id = input("Enter student ID:")
    name = input("Enter student name:")
    department = input("Enter department:")
    year = input("Enter year of study:")

    with open(FILE_PATH,"a", newline='') as file:
        Writer = csv.writer(file)
        Writer.writerow([student_id,name,department,year])

    print("Student added successfully.")

def list_students():
    if not os.path.exists(FILE_PATH):
        print("No student records found :")
        return
    with open(FILE_PATH, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)