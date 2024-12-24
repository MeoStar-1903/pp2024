import curses

def list_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(0, 0, "Courses:")
    for course in courses:
        stdscr.addstr(f"ID: {course[0]}, Name: {course[1]}\n")
    stdscr.refresh()

def list_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr(0, 0, "Students:")
    for student in students:
        stdscr.addstr(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}\n")
    stdscr.refresh()

def show_student_marks(stdscr, marks, course_id):
    stdscr.clear()
    if course_id in marks:
        stdscr.addstr(0, 0, f"Marks for course {course_id}:")
        for student_id, mark in marks[course_id].items():
            stdscr.addstr(f"Student ID: {student_id}, Mark: {mark}\n")
    else:
        stdscr.addstr(0, 0, f"No marks found for course {course_id}")
    stdscr.refresh()
