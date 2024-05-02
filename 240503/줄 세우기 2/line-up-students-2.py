class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

N = int(input())
studentArr = []

for i in range(N):
    tempArr = input().split()
    height = int(tempArr[0])
    weight = int(tempArr[1])

    studentArr.append(Student(height, weight, i+1))

studentArr.sort(key = lambda x: (x.height, -x.weight))

for elem in studentArr:
    print(elem.height, elem.weight, elem.number)