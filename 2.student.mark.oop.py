# Input functions
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

# Listing functions
def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def show_student_marks(marks, course_id):
    if course_id in marks:
        print(f"Marks for course {course_id}:")
        for student_id, mark in marks[course_id].items():
            print(f"Student ID: {student_id}, Mark: {mark}")
    else:
        print(f"No marks found for course {course_id}")

# Main program
students = input_student_info()
courses = input_course_info()
marks = input_marks(students, courses)

list_courses(courses)
list_students(students)
course_id = input("Enter course ID to show marks: ")
show_student_marks(marks, course_id)



class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def input(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter student name: ")
        self.dob = input("Enter student Date of Birth (DoB): ")

    def list(self):
        print(f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}")

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def input(self):
        self.id = input("Enter course ID: ")
        self.name = input("Enter course name: ")

    def list(self):
        print(f"ID: {self.id}, Name: {self.name}")

class StudentMark:
    def __init__(self, student_id, course_id, mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark

    def input(self):
        self.student_id = input("Enter student ID: ")
        self.course_id = input("Enter course ID: ")
        self.mark = float(input("Enter mark: "))

    def list(self):
        print(f"Student ID: {self.student_id}, Course ID: {self.course_id}, Mark: {self.mark}")


students = []
courses = []
marks = []

# Input students
num_students = int(input("Enter number of students: "))
for _ in range(num_students):
    student = Student("", "", "")
    student.input()
    students.append(student)

# Input courses
num_courses = int(input("Enter number of courses: "))
for _ in range(num_courses):
    course = Course("", "")
    course.input()
    courses.append(course)

# Input marks
for course in courses:
    for student in students:
        mark = StudentMark(student.id, course.id, 0)
        mark.input()
        marks.append(mark)

# List courses
for course in courses:
    course.list()

# List students
for student in students:
    student.list()

# Show marks for a given course
course_id = input("Enter course ID to show marks: ")
for mark in marks:
    if mark.course_id == course_id:
        mark.list()

