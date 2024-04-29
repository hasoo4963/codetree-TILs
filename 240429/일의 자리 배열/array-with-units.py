userInput = input().split()
pp = int(userInput[0])
p = int(userInput[1])

arr = [pp, p, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(2, 10):
    temp = arr[i-1] + arr[i-2]
    temp = temp % 10
    arr[i] = temp

print(*arr)