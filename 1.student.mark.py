def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (DD/MM/YYYY): ")
    return (student_id, name, dob)

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return (course_id, name)

def input_marks(course_id, students):
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for {student[1]} in course {course_id}: "))
        marks[student[0]] = mark
    return marks
def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def show_student_marks(course_id, marks):
    print(f"Marks for course {course_id}:")
    for student_id, mark in marks.items():
        print(f"Student ID: {student_id}, Mark: {mark}")
def main():
    students = []
    courses = []
    marks = {}

    num_students = input_number_of_students()
    for _ in range(num_students):
        students.append(input_student_info())

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        courses.append(input_course_info())

    for course in courses:
        course_id = course[0]
        marks[course_id] = input_marks(course_id, students)

    list_courses(courses)
    list_students(students)
    for course in courses:
        show_student_marks(course[0], marks[course[0]])

if __name__ == "__main__":
    main()
