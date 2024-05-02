class point:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number

N = int(input())
pointArr = []
for i in range(N):
    tempArr = input().split()
    pointArr.append(point(int(tempArr[0]), int(tempArr[1]), i + 1))

pointArr.sort(key = lambda point: (point.x + point.y, point.number))

for i in range(N):
    print(pointArr[i].number)