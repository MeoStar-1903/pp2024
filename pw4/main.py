import curses
import numpy as np
from input import input_student_info, input_course_info, input_marks
from output import list_courses, list_students, show_student_marks
from domains.student import Student
from domains.course import Course
from domains.student_mark import StudentMark

def main(stdscr):
    students = input_student_info()
    courses = input_course_info()
    marks = input_marks(students, courses)

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Student Mark Management System")
        stdscr.addstr(2, 0, "1. List Courses")
        stdscr.addstr(3, 0, "2. List Students")
        stdscr.addstr(4, 0, "3. Show Student Marks for a Given Course")
        stdscr.addstr(5, 0, "4. Calculate and Display GPA for Each Student")
        stdscr.addstr(6, 0, "5. Sort Students by GPA")
        stdscr.addstr(7, 0, "6. Exit")
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('1'):
            list_courses(stdscr, courses)
        elif key == ord('2'):
            list_students(stdscr, students)
        elif key == ord('3'):
            course_id = stdscr.getstr(0, 0, "Enter course ID to show marks: ").decode()
            show_student_marks(stdscr, marks, course_id)
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



