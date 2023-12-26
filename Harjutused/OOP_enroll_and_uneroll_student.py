"""
Kirjuta meetod enroll_student, mis lisab tudengi kui ta pole veel lisatud. Lisa meetod unenroll_student,
mis kustutab tudengi kui ta on lisatud. Lisa meetod add_couse, mis lisab kursuse dict-i,
kus võtmeks on id ja väärtuseks on kursus
"""


class Course:
    def __init__(self, course_id: int, course_name: str):
        self.course_id = course_id
        self.course_name = course_name
        self.students = []

    def enroll_student(self, student_name: str):
        if student_name not in self.students:
            self.students.append(student_name)

    def unenroll_student(self, student_name: str):
        if student_name in self.students:
            self.students.remove(student_name)


class ElearningPlatform:
    def __init__(self):
        self.courses = {}

    def add_course(self, course: Course):
        self.courses[course.course_id] = course


platform = ElearningPlatform()
course1 = Course("101", "Python Programming")
print(course1)
platform.add_course(course1)

print(course1 in platform.courses.values())