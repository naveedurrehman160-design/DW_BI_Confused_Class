print("===================================")
print("        GPA CALCULATOR")
print("===================================")

num_courses = int(input("Enter number of courses: "))

courses = []

print("\nEnter course details:")
print("-" * 60)

for i in range(num_courses):
    print(f"\nCourse {i + 1}")

    name = input("Course Name: ")
    credit = float(input("Credit Hours: "))
    marks = float(input("Obtained Marks: "))

    courses.append([name, credit, marks])

print("\n")
print("=" * 70)
print(f"{'Course':<25}{'Credit Hours':<15}{'Marks':<10}{'Grade':<10}{'GP':<10}")
print("=" * 70)

total_points = 0
total_credits = 0

for course in courses:

    name = course[0]
    credit = course[1]
    marks = course[2]

    if marks >= 90:
        grade = "A+"
        gp = 4.00
    elif marks >= 80:
        grade = "A"
        gp = 4.00
    elif marks >= 78:
        grade = "A-"
        gp = 3.67
    elif marks >= 75:
        grade = "B+"
        gp = 3.33
    elif marks >= 70:
        grade = "B"
        gp = 3.00
    elif marks >= 65:
        grade = "B-"
        gp = 2.67
    elif marks >= 60:
        grade = "C+"
        gp = 2.33
    elif marks >= 55:
        grade = "C"
        gp = 2.00
    elif marks >= 50:
        grade = "C-"
        gp = 1.67
    else:
        grade = "F"
        gp = 0.00

    points = credit * gp

    total_points += points
    total_credits += credit

    print(f"{name:<25}{credit:<15}{marks:<10}{grade:<10}{gp:<10}")

print("=" * 70)

gpa = total_points / total_credits

print(f"\nTotal Credit Hours: {total_credits}")
print(f"GPA: {gpa:.2f}")

if gpa >= 3.5:
    print("Excellent Performance! 🎉")
elif gpa >= 3.0:
    print("Very Good Performance! 👍")
elif gpa >= 2.5:
    print("Good Performance!")
else:
    print("Keep Working Hard!")