def isEqual(arr1, arr2, n):
    for i in range(n):
        if arr1[i] != arr2[i]:
            return False
    return True

arr = input().split()
n = int(arr[0])
k = int(arr[1])
T = list(arr[2])

userInput = [ input() for _ in range(n) ]
equalResult = []
for i in range(n):
    if isEqual(T, userInput[i], len(T)):
        equalResult.append(userInput[i])

equalResult.sort()
print(equalResult[k-1])