import tkinter as tk
from tkinter import messagebox

courses = []

def get_grade(marks):
    if marks >= 90:
        return "A+", 4.0
    elif marks >= 80:
        return "A", 4.0
    elif marks >= 78:
        return "A-", 3.7
    elif marks >= 75:
        return "B+", 3.3
    elif marks >= 70:
        return "B", 3.0
    elif marks >= 65:
        return "B-", 2.7
    elif marks >= 60:
        return "C+", 2.3
    elif marks >= 55:
        return "C", 2.0
    elif marks >= 50:
        return "C-", 1.7
    elif marks >= 40:
        return "D", 1.0
    else:
        return "F", 0.0


def add_course():
    name = name_entry.get()
    credit = credit_entry.get()
    marks = marks_entry.get()

    if name == "" or credit == "" or marks == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        credit = float(credit)
        marks = float(marks)
    except:
        messagebox.showerror("Error", "Credit hours and marks must be numbers")
        return

    if marks < 0 or marks > 100:
        messagebox.showerror("Error", "Marks must be between 0 and 100")
        return

    grade, points = get_grade(marks)

    courses.append((name, credit, marks, grade, points))

    course_list.insert(
        tk.END,
        f"{name} | {credit} CH | {marks} Marks | {grade}"
    )

    name_entry.delete(0, tk.END)
    credit_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)


def calculate_gpa():
    if len(courses) == 0:
        messagebox.showerror("Error", "Please add at least one course")
        return

    total_points = 0
    total_credits = 0

    for name, credit, marks, grade, points in courses:
        total_points += credit * points
        total_credits += credit

    gpa = total_points / total_credits

    result_label.config(text=f"GPA: {gpa:.3f}")


def reset():
    courses.clear()
    course_list.delete(0, tk.END)
    result_label.config(text="GPA: 0.000")


window = tk.Tk()
window.title("GPA Calculator")
window.geometry("600x600")

title = tk.Label(
    window,
    text="GPA Calculator",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

tk.Label(window, text="Course Name").pack()
name_entry = tk.Entry(window, width=40)
name_entry.pack(pady=5)

tk.Label(window, text="Credit Hours").pack()
credit_entry = tk.Entry(window, width=40)
credit_entry.pack(pady=5)

tk.Label(window, text="Obtained Marks").pack()
marks_entry = tk.Entry(window, width=40)
marks_entry.pack(pady=5)

add_button = tk.Button(
    window,
    text="Add Course",
    command=add_course,
    width=20
)
add_button.pack(pady=15)

course_list = tk.Listbox(
    window,
    width=65,
    height=10
)
course_list.pack(pady=10)

calculate_button = tk.Button(
    window,
    text="Calculate GPA",
    command=calculate_gpa,
    width=20
)
calculate_button.pack(pady=10)

result_label = tk.Label(
    window,
    text="GPA: 0.000",
    font=("Arial", 20, "bold")
)
result_label.pack(pady=10)

reset_button = tk.Button(
    window,
    text="Reset",
    command=reset,
    width=20
)
reset_button.pack(pady=10)

window.mainloop()