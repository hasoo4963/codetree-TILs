N = int(input())
arr = input().split()

for i in range(2*N):
    arr[i] = int(arr[i])
arr.sort()


left = 0
right = (2*N) - 1
resultArr = []
for i in range(N):
    resultArr.append(arr[left] + arr[right])
    left += 1
    right -= 1

resultArr.sort()
print(resultArr[N-1])