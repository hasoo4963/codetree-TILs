arr = input().split()
N = int(arr[0])
k = int(arr[1])

userInput = input().split()
for elem in userInput:
    elem = int(elem)

userInput.sort()
print(userInput[k-1])