students = []
def log_activity(func):
    def wrapper(*args, **kwargs):
        print("\n[LOG] Function is starting...")
        result = func(*args, **kwargs)
        print("[LOG] Function finished successfully.\n")
        return result
    return wrapper

@log_activity
def add_student(name, roll_number, *marks, **other_info):
    total = sum(marks)
    average = total / len(marks) if marks else 0

    student = {
        "name": name,
        "roll_number": roll_number,
        "marks": list(marks),
        "total": total,
        "average": average
    }

    for key in other_info:
        student[key] = other_info[key]

    students.append(student)
    print(f"Student '{name}' added.")

@log_activity
def display_students():
    if not students:
        print("No student data found.")
        return

    print("\n===== Student Records =====")
    for student in students:
        print(f"\nName      : {student['name']}")
        print(f"Roll No.  : {student['roll_number']}")
        print(f"Marks     : {student['marks']}")
        print(f"Total     : {student['total']}")

display_students()