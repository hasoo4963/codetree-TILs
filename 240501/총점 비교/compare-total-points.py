class Student:
    def __init__(self, name , kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math
        self.name = name

students = []
N = int(input())
for i in range(N):
    name, kor, eng, math = input().split()
    students.append(Student(name, int(kor), int(eng), int(math)))

students.sort(key=lambda x: x.kor + x.eng + x.math) 

for student in students: 
    print(student.name, student.kor, student.eng, student.math)