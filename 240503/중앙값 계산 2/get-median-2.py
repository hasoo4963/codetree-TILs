def calculateCenter(arr, resultArr):
    centerIdx = len(arr) // 2
    resultArr.append(arr[centerIdx])

n = int(input())
inputArr = input().split()
tempArr = []
resultArr = []

for i in range(n):
    temp = int(inputArr[i])

    if i % 2 == 0:
        tempArr.append(temp)
        tempArr.sort()
        calculateCenter(tempArr, resultArr)
    else:
        tempArr.append(temp)

print(*resultArr)