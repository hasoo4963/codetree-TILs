# n = 4
# arr = [1, 5, 2, 6]

# max_sum = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             arr[i], arr[j], arr[k] = arr[i] * 2, arr[j] * 2, arr[k] * 2

#             sum_diff = 0
#             for l in range(n - 1):
#                 sum_diff += abs(arr[l + 1] - arr[l])

#             max_sum = max(max_sum, sum_diff)
#             arr[i], arr[j], arr[k] = arr[i] // 2, arr[j] // 2, arr[k] // 2

# print(max_sum)

# >> 26

N = int(input())
arr = []
arr = list(map(int, input().split()))

answer = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i] <= arr[j] and arr[j] <= arr[k]:
                answer += 1
print(answer)