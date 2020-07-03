# isinstance()

class Student:
    def __init__(self):
        pass

student = Student()

print(isinstance(student, Student))
print()

class Student:
    def study(self):
        print("공부하장")

class Teacher:
    def teach(self):
        print("학생을 가르치자")

classroom = [Student(), Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()