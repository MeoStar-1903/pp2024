def input_number_of_students():
    return int(input("Enter number of students in the class: "))

def input_student_info():
    students = []
    num_students = input_number_of_students()
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DoB): ")
        students.append((student_id, name, dob))
    return students

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_course_info():
    courses = []
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append((course_id, name))
    return courses

def input_marks(students, courses):
    marks = {}
    for course in courses:
        course_id = course[0]
        marks[course_id] = {}
        for student in students:
            student_id = student[0]
            mark = float(input(f"Enter mark for student {student_id} in course {course_id}: "))
            marks[course_id][student_id] = mark
    return marks
