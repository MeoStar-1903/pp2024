class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def input(self):
        self.id = input("Enter course ID: ")
        self.name = input("Enter course name: ")

    def list(self):
        print(f"ID: {self.id}, Name: {self.name}")
