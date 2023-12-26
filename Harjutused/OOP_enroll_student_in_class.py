"""
Kirjuta meetod enroll_student_in_class, mis lisab õpilase klassi, kui selline õpilane on olemas (kasuta meetodit enroll)
"""


class Student:
    def __init__(self, name: str):
        self.name = name
        self.classes = []

    def enroll(self, class_name: str):
        self.classes.append(class_name)

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def enroll_student_in_class(self, student_name: str, class_name: str):
        for student in self.students:
            if student.name == student_name:
                student.enroll(class_name)
                break


school = School("Lincoln High School")
student1 = Student("Alice")
school.add_student(student1)

school.enroll_student_in_class("Alice", "Biology")
print("Biology" in student1.classes)