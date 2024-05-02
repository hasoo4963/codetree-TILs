arr = input().split()
N = int(arr[0])
k = int(arr[1])

userInput = input().split()
for i in range(N):
    userInput[i] = int(userInput[i])

userInput.sort()
print(userInput[k-1])