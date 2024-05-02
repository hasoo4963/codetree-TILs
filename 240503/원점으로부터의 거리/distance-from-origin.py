class point:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number

N = int(input())
pointArr = []
for i in range(N):
    tempArr = input().split()
    
    x = int(tempArr[0])
    y = int(tempArr[1])

    if x < 0:
        x *= -1
    if y < 0:
        y *= -1
    pointArr.append(point(x, y, i + 1))

pointArr.sort(key = lambda point: (point.x + point.y, point.number))

for i in range(N):
    print(pointArr[i].number)