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
