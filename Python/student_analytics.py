from functools import reduce

# Fixed subject names stored in a tuple
SUBJECTS = ("Python", "Java", "SQL", "Aptitude")

# Student records stored in a list of dictionaries
students = [
    {
        "id": 101,
        "name": "Rahul",
        "marks": [95, 90, 88, 97]
    },
    {
        "id": 102,
        "name": "Priya",
        "marks": [90, 85, 92, 89]
    },
    {
        "id": 103,
        "name": "Arjun",
        "marks": [65, 70, 75, 68]
    },
    {
        "id": 104,
        "name": "Sneha",
        "marks": [98, 96, 94, 99]
    },
    {
        "id": 105,
        "name": "Kiran",
        "marks": [35, 40, 28, 45]
    },
    {
        "id": 106,
        "name": "Rahul",
        "marks": [80, 82, 85, 78]
    }
]


# Calculate the average using reduce()
def calculate_average(marks):
    total = reduce(lambda a, b: a + b, marks, 0)
    return total / len(marks)


# Assign a grade based on average marks
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


# Display all students
def display_students():
    print("\n========== ALL STUDENTS ==========")

    for student in students:
        average = calculate_average(student["marks"])

        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Marks: {student['marks']} | "
            f"Average: {average:.2f}"
        )


# Calculate averages using map()
def display_averages():
    print("\n========== STUDENT AVERAGES ==========")

    averages = list(
        map(
            lambda student: {
                "name": student["name"],
                "average": calculate_average(student["marks"])
            },
            students
        )
    )

    for result in averages:
        print(
            f"{result['name']}: "
            f"{result['average']:.2f}"
        )


# Filter students who passed
def display_passed_students():
    print("\n========== PASSED STUDENTS ==========")

    passed = list(
        filter(
            lambda student: all(
                mark >= 35 for mark in student["marks"]
            ),
            students
        )
    )

    for student in passed:
        print(
            f"{student['name']} - "
            f"Average: {calculate_average(student['marks']):.2f}"
        )


# Display top performers using filter()
def display_top_performers():
    print("\n========== TOP PERFORMERS ==========")

    top_performers = list(
        filter(
            lambda student: calculate_average(student["marks"]) >= 85,
            students
        )
    )

    if not top_performers:
        print("No top performers found.")
        return

    for student in top_performers:
        average = calculate_average(student["marks"])

        print(
            f"Name: {student['name']} | "
            f"Average: {average:.2f} | "
            f"Grade: {calculate_grade(average)}"
        )


# Find the class topper
def find_class_topper():
    print("\n========== CLASS TOPPER ==========")

    topper = max(
        students,
        key=lambda student: calculate_average(student["marks"])
    )

    average = calculate_average(topper["marks"])

    print(f"Name: {topper['name']}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {calculate_grade(average)}")


# Calculate subject-wise averages
def subject_wise_analysis():
    print("\n========== SUBJECT-WISE ANALYSIS ==========")

    for index, subject in enumerate(SUBJECTS):
        marks = [student["marks"][index] for student in students]

        average = reduce(lambda a, b: a + b, marks, 0) / len(marks)

        print(f"{subject}: Average = {average:.2f}")


# Search student by name
def search_student():
    name = input("Enter student name: ").strip()

    results = list(
        filter(
            lambda student: student["name"].casefold() == name.casefold(),
            students
        )
    )

    if results:
        for student in results:
            average = calculate_average(student["marks"])

            print(f"\nID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            print(f"Average: {average:.2f}")
            print(f"Grade: {calculate_grade(average)}")
    else:
        print("Student not found.")


# Generate a report using list comprehension
def performance_report():
    print("\n========== PERFORMANCE REPORT ==========")

    report = [
        {
            "id": student["id"],
            "name": student["name"],
            "average": calculate_average(student["marks"]),
            "grade": calculate_grade(
                calculate_average(student["marks"])
            )
        }
        for student in students
    ]

    # Sort report by average in descending order
    report.sort(key=lambda item: item["average"], reverse=True)

    for item in report:
        print(
            f"ID: {item['id']} | "
            f"Name: {item['name']} | "
            f"Average: {item['average']:.2f} | "
            f"Grade: {item['grade']}"
        )


# Use a set to find unique student names
def display_unique_names():
    print("\n========== UNIQUE STUDENT NAMES ==========")

    unique_names = {student["name"] for student in students}

    for name in sorted(unique_names):
        print(name)


# Calculate the sum of all marks using reduce()
def calculate_total_marks():
    print("\n========== TOTAL CLASS MARKS ==========")

    total = reduce(
        lambda accumulator, student:
            accumulator + sum(student["marks"]),
        students,
        0
    )

    print(f"Total marks scored by all students: {total}")


# Main menu
def main():
    while True:
        print("\n===== STUDENT PERFORMANCE ANALYTICS =====")
        print("1. Display All Students")
        print("2. Calculate Student Averages")
        print("3. Display Passed Students")
        print("4. Display Top Performers")
        print("5. Subject-wise Analysis")
        print("6. Find Class Topper")
        print("7. Search Student")
        print("8. Display Performance Report")
        print("9. Display Unique Student Names")
        print("10. Calculate Total Class Marks")
        print("11. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                display_students()

            elif choice == 2:
                display_averages()

            elif choice == 3:
                display_passed_students()

            elif choice == 4:
                display_top_performers()

            elif choice == 5:
                subject_wise_analysis()

            elif choice == 6:
                find_class_topper()

            elif choice == 7:
                search_student()

            elif choice == 8:
                performance_report()

            elif choice == 9:
                display_unique_names()

            elif choice == 10:
                calculate_total_marks()

            elif choice == 11:
                print("Thank you for using the application!")
                break

            else:
                print("Invalid choice. Select a number from 1 to 11.")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()