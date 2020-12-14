#클래스를 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

#학생 리스트를 선언
students = [
    Student("남진주", 95, 96, 97, 100),
    Student("스완", 95, 96, 97, 95),
    Student("루시우", 45, 12, 85, 44)
]

print("이름", "총점", "평균", sep="\t")

#for student in students:
#    print(student.to_string()) # 메소드 사용법 제대로 익히기

for student in students:
    print(str(student))

student.





