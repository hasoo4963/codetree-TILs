class BodyInfo:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def print(self):
        print(self.name, self.height, self.weight)

n = int(input())
studentArr = []

for i in range(n):
    tempArr = input().split()
    studentArr.append(BodyInfo(tempArr[0], int(tempArr[1]), int(tempArr[2])))

studentArr.sort(key = lambda x : (x.height, -x.weight))

for i in range(n):
    studentArr[i].print()