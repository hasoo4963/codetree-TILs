import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

min_val = sys.maxsize
for i in range(N):
    for j in range(i+1, N):
        temp = 0
        for k in range(N):
            if k == i or k == j:
                continue
            temp += arr[k]
        min_val = min(min_val, abs(S-temp))
print(min_val)