
from functools import reduce

# ==================================================
# 1. DATA STRUCTURES
# ==================================================

# Tuple: Store fixed subject names
SUBJECTS = ("Python", "Java", "SQL", "Aptitude")

# List of dictionaries: Store student records
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


# ==================================================
# 2. CALCULATE AVERAGE AND GRADE
# ==================================================

def calculate_average(marks):
    if not marks:
        return 0.0
    total = reduce(lambda a, b: a + b, marks, 0)
    return total / len(marks)


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


# ==================================================
# 3. DISPLAY ALL STUDENTS
# ==================================================

def display_students():
    print("\n========== ALL STUDENTS ==========")

    if not students:
        print("No student records found.")
        return

    for student in students:
        average = calculate_average(student["marks"])

        print(f"\nID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {calculate_grade(average)}")


# ==================================================
# 4. CALCULATE AVERAGES USING MAP()
# ==================================================

def display_averages():
    print("\n========== STUDENT AVERAGES ==========")

    if not students:
        print("No student records found.")
        return

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


# ==================================================
# 5. DISPLAY PASSED STUDENTS USING FILTER()
# ==================================================

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

    if not passed:
        print("No passed students found.")
        return

    for student in passed:
        average = calculate_average(student["marks"])

        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Average: {average:.2f}"
        )


# ==================================================
# 6. DISPLAY FAILED STUDENTS
# ==================================================

def display_failed_students():
    print("\n========== FAILED STUDENTS ==========")

    failed = list(
        filter(
            lambda student: any(
                mark < 35 for mark in student["marks"]
            ),
            students
        )
    )

    if not failed:
        print("No failed students found.")
        return

    for student in failed:
        failed_subjects = [
            SUBJECTS[index] if index < len(SUBJECTS) else f"Subject {index+1}"
            for index, mark in enumerate(student["marks"])
            if mark < 35
        ]

        print(f"\nID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Failed Subjects: {', '.join(failed_subjects)}")
        print(f"Marks: {student['marks']}")


# ==================================================
# 7. DISPLAY TOP PERFORMERS
# ==================================================

def display_top_performers():
    print("\n========== TOP PERFORMERS ==========")

    top_performers = list(
        filter(
            lambda student: calculate_average(
                student["marks"]
            ) >= 85,
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


# ==================================================
# 8. FIND CLASS TOPPER
# ==================================================

def find_class_topper():
    print("\n========== CLASS TOPPER ==========")

    if not students:
        print("No student records found.")
        return

    topper = max(
        students,
        key=lambda student: calculate_average(student["marks"])
    )

    average = calculate_average(topper["marks"])

    print(f"ID: {topper['id']}")
    print(f"Name: {topper['name']}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {calculate_grade(average)}")


# ==================================================
# 9. SUBJECT-WISE ANALYSIS USING REDUCE()
# ==================================================

def subject_wise_analysis():
    print("\n========== SUBJECT-WISE ANALYSIS ==========")

    if not students:
        print("No student records found.")
        return

    for index, subject in enumerate(SUBJECTS):

        marks = [
            student["marks"][index]
            for student in students
            if index < len(student["marks"])
        ]

        if not marks:
            print(f"{subject}: No marks available")
            continue

        total = reduce(lambda a, b: a + b, marks, 0)
        average = total / len(marks)

        print(f"{subject}: Average = {average:.2f}")


# ==================================================
# 10. SEARCH STUDENT
# ==================================================

def search_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    results = list(
        filter(
            lambda student: student["name"].casefold()
            == name.casefold(),
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


# ==================================================
# 11. PERFORMANCE REPORT USING LIST COMPREHENSION
# ==================================================

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

    report.sort(
        key=lambda item: item["average"],
        reverse=True
    )

    print(
        f"{'ID':<8}"
        f"{'NAME':<15}"
        f"{'AVERAGE':<12}"
        f"{'GRADE':<10}"
    )

    print("-" * 45)

    for item in report:
        print(
            f"{item['id']:<8}"
            f"{item['name']:<15}"
            f"{item['average']:<12.2f}"
            f"{item['grade']:<10}"
        )


# ==================================================
# 12. UNIQUE STUDENT NAMES USING SET
# ==================================================

def display_unique_names():
    print("\n========== UNIQUE STUDENT NAMES ==========")

    unique_names = {
        student["name"]
        for student in students
    }

    for name in sorted(unique_names):
        print(name)

    print(f"Total unique names: {len(unique_names)}")


# ==================================================
# 13. TOTAL CLASS MARKS USING REDUCE()
# ==================================================

def calculate_total_marks():
    print("\n========== TOTAL CLASS MARKS ==========")

    total = reduce(
        lambda accumulator, student:
        accumulator + sum(student["marks"]),
        students,
        0
    )

    print(f"Total students: {len(students)}")
    print(f"Total subjects: {len(SUBJECTS)}")
    print(f"Total marks scored: {total}")


# ==================================================
# 14. ADD A NEW STUDENT
# ==================================================

def add_student():
    print("\n========== ADD NEW STUDENT ==========")

    try:
        student_id = int(input("Enter student ID: "))

        if any(student["id"] == student_id for student in students):
            print("This student ID already exists.")
            return

        name = input("Enter student name: ").strip()

        if not name:
            print("Student name cannot be empty.")
            return

        marks = []

        for subject in SUBJECTS:
            while True:
                try:
                    mark = int(input(f"Enter {subject} marks (0-100): "))

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break

                    print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid integer.")

        students.append({
            "id": student_id,
            "name": name,
            "marks": marks
        })

        print(f"Student {name} added successfully!")

    except ValueError:
        print("Invalid student ID. Please enter an integer.")


# ==================================================
# 15. UPDATE STUDENT MARKS
# ==================================================

def update_student_marks():
    print("\n========== UPDATE STUDENT MARKS ==========")

    try:
        student_id = int(input("Enter student ID: "))

    except ValueError:
        print("Please enter a valid student ID.")
        return

    student = next(
        (
            item for item in students
            if item["id"] == student_id
        ),
        None
    )

    if student is None:
        print("Student not found.")
        return

    print(f"Student: {student['name']}")

    updated_marks = []
    for index, subject in enumerate(SUBJECTS):
        while True:
            try:
                mark = int(
                    input(
                        f"Enter new {subject} marks "
                        f"(0-100): "
                    )
                )

                if 0 <= mark <= 100:
                    updated_marks.append(mark)
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid integer.")

    student["marks"] = updated_marks
    print("Student marks updated successfully!")


# ==================================================
# 16. MAIN MENU
# ==================================================

def main():
    while True:
        print("\n" + "=" * 55)
        print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
        print("=" * 55)

        print("1.  Display All Students")
        print("2.  Calculate Student Averages")
        print("3.  Display Passed Students")
        print("4.  Display Top Performers")
        print("5.  Subject-Wise Analysis")
        print("6.  Find Class Topper")
        print("7.  Search Student")
        print("8.  Display Performance Report")
        print("9.  Display Unique Student Names")
        print("10. Calculate Total Class Marks")
        print("11. Display Failed Students")
        print("12. Add New Student")
        print("13. Update Student Marks")
        print("14. Exit")

        print("=" * 55)

        try:
            choice = int(input("Enter your choice (1-14): "))

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
                display_failed_students()

            elif choice == 12:
                add_student()

            elif choice == 13:
                update_student_marks()

            elif choice == 14:
                print("Thank you for using the application!")
                break

            else:
                print("Invalid choice. Select a number from 1 to 14.")

        except ValueError:
            print("Invalid input. Please enter a number.")

        except (EOFError, KeyboardInterrupt):
            print("\nApplication terminated.")
            break


# ==================================================
# 17. APPLICATION ENTRY POINT
# ==================================================

if __name__ == "__main__":
    main()
