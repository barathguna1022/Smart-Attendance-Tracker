import csv

FILE_PATH = "data/performance.csv"

def add_performance():
    student_id = input("Enter Student ID: ")
    test_name = input("Enter Test Name: ")
    score = float(input("Enter Score: "))
    max_score = float(input("Enter Max Score: "))

    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, test_name, score, max_score])

    print("Performance record added successfully.")


def calculate_average(student_id):
    total_score = 0
    total_max = 0

    with open(FILE_PATH, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            if row[0] == student_id:
                total_score += float(row[2])
                total_max += float(row[3])

    if total_max == 0:
        return None, None

    percentage = (total_score / total_max) * 100

    if percentage >= 85:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 55:
        grade = "C"
    else:
        grade = "D"

    return percentage, grade
