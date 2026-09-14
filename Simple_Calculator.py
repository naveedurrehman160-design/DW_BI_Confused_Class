print("===== GPA CALCULATOR =====")

courses = int(input("Enter number of courses: "))

total_points = 0
total_credits = 0

grade_points = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D": 1.0,
    "F": 0.0
}

for i in range(courses):

    print("\nCourse", i + 1)

    name = input("Course name: ")
    credit = float(input("Credit hours: "))
    grade = input("Grade: ").upper()

    points = grade_points[grade]

    total_points += points * credit
    total_credits += credit

gpa = total_points / total_credits

print("\n==========================")
print("Your GPA is:", round(gpa, 2))
print("==========================")