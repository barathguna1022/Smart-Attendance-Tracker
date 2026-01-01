import csv
import os

FILE_PATH = "data/attendance.csv"


def mark_attendance():
    student_id = input("Enter Student ID: ")
    date = input("Enter date (YYYY-MM-DD): ")
    status = input("Enter status (P/A): ").upper()

    file_exists = os.path.exists(FILE_PATH)

    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["student_id", "date", "status"])

        writer.writerow([student_id, date, status])

    print("Attendance marked successfully.")


def view_attendance():
    if not os.path.exists(FILE_PATH):
        print("No attendance records found.")
        return

    with open(FILE_PATH, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\nStudent ID | Date       | Status")
        print("-------------------------------")
        for row in reader:
            print(f"{row[0]:10} | {row[1]:10} | {row[2]}")
