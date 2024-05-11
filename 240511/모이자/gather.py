import sys

n = int(input())
arr = list(map(int,input().split()))

# result = []

# min_val = 100000
# for i in range(n): # i번째 집으로 모이면,
#     sum = 0
#     for j in range(i + 1, n):
#         diff = j - i
#         sum = sum + (diff * arr[j])

#     for k in range(i):
#         diff = i - k
#         sum = sum + (diff * arr[k])

#     result.append(sum)

# print(min(result))

min_val = sys.maxsize

for i in range(n):
    sum = 0
    for j in range(n):
        diff = abs(i - j) * arr[j]
        sum += diff

    min_val = min(min_val, sum)

print(min_val)