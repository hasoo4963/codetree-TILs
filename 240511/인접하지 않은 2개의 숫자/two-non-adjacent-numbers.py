import sys
n = int(input())
arr = list(map(int, input().split()))

max_val = -sys.maxsize
for i in range(n):
    temp = 0
    for j in range(i+2, n):
        temp = arr[i] + arr[j]
    max_val = max(max_val, temp)
print(max_val)