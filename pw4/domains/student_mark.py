import math

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
