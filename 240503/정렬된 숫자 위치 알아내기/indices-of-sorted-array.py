class Element:
    def __init__(self, value, originPosition):
        self.value = value
        self.originPosition = originPosition
        

N = int(input())
tempArr = input().split()
userInput = []
resultArr = [ 0 for _ in range(N) ]

for i in range(N):
    elem = Element(int(tempArr[i]), i)
    userInput.append(elem)

userInput.sort(key = lambda x: (x.value, x.originPosition))

# for i in range(N):
#     print(userInput[i].value, userInput[i].originPosition)

for i in range(N):
    resultArr[userInput[i].originPosition] = i + 1

print(*resultArr)