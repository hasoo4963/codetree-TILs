class Body:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def print(self):
        print(self.name, self.height, self.weight)

N = int(input())
bodyArr = []
for i in range(N):
    name, height, weight = tuple(map(str,input().split()))
    bodyArr.append(Body(name, int(height), int(weight)))
# bodyArr = [
#     Body(map(str, input().split()))
#     for i in range(N)
# ]

bodyArr.sort(key = lambda Body: Body.height)

for bd in bodyArr:
    bd.print()