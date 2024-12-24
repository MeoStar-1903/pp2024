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

import math
import numpy as np
import curses



#Classes with Updated Methods
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = []
        self.marks = []

    def input(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter student name: ")
        self.dob = input("Enter student Date of Birth (DoB): ")

    def list(self):
        print(f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}")

    def add_course(self, course_id, mark):
        self.courses.append(course_id)
        self.marks.append(mark)

    def calculate_gpa(self):
        if len(self.marks) == 0:
            return 0
        return np.average(self.marks)

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
        self.mark = math.floor(mark * 10) / 10

    def input(self):
        self.student_id = input("Enter student ID: ")
        self.course_id = input("Enter course ID: ")
        self.mark = math.floor(float(input("Enter mark: ")) * 10) / 10

    def list(self):
        print(f"Student ID: {self.student_id}, Course ID: {self.course_id}, Mark: {self.mark}")




#Main Program with GPA Calculation and Sorting
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
        student.add_course(course.id, mark.mark)

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

# Calculate and display GPA for each student
for student in students:
    gpa = student.calculate_gpa()
    print(f"Student ID: {student.id}, GPA: {gpa}")

# Sort students by GPA in descending order
students.sort(key=lambda x: x.calculate_gpa(), reverse=True)

# List students sorted by GPA
print("Students sorted by GPA:")
for student in students:
    student.list()
    print(f"GPA: {student.calculate_gpa()}")



#Decorate UI with curses Module
def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(0, 0, "Student Mark Management System")
    stdscr.addstr(2, 0, "1. List Courses")
    stdscr.addstr(3, 0, "2. List Students")
    stdscr.addstr(4, 0, "3. Show Student Marks for a Given Course")
    stdscr.addstr(5, 0, "4. Calculate and Display GPA for Each Student")
    stdscr.addstr(6, 0, "5. Sort Students by GPA")
    stdscr.addstr(7, 0, "6. Exit")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('1'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Courses:")
            for course in courses:
                stdscr.addstr(f"ID: {course.id}, Name: {course.name}\n")
            stdscr.refresh()
        elif key == ord('2'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Students:")
            for student in students:
                stdscr.addstr(f"ID: {student.id}, Name: {student.name}, DoB: {student.dob}\n")
            stdscr.refresh()
        elif key == ord('3'):
            stdscr.clear()
            course_id = stdscr.getstr(0, 0, "Enter course ID to show marks: ").decode()
            stdscr.addstr(1, 0, f"Marks for course {course_id}:")
            for mark in marks:
                if mark.course_id == course_id:
                    stdscr.addstr(f"Student ID: {mark.student_id}, Mark: {mark.mark}\n")
            stdscr.refresh()
        elif key == ord('4'):
            stdscr.clear()
            for student in students:
                gpa = student.calculate_gpa()
                stdscr.addstr(f"Student ID: {student.id}, GPA: {gpa}\n")
            stdscr.refresh()
        elif key == ord('5'):
            stdscr.clear()
            students.sort(key=lambda x: x.calculate_gpa(), reverse=True)
            stdscr.addstr(0, 0, "Students sorted by GPA:")
            for student in students:
                stdscr.addstr(f"ID: {student.id}, Name: {student.name}, GPA: {student.calculate_gpa()}\n")
            stdscr.refresh()
        elif key == ord('6'):
            break

curses.wrapper(main)
