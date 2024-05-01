class Body:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

N = int(input())
bodyArr = []
for i in range(N):
    height, weight = input().split()
    bodyArr.append(Body(int(height),int(weight),i+1))

bodyArr.sort(key = lambda x : (-x.height, -x.weight, -x.number))

for bd in bodyArr:
    print(bd.height, bd.weight, bd.number)