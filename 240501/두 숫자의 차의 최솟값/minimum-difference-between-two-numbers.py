n = int(input())
arr = list(map(int, input().split()))

min_dif = 101
for i in range(n):
    for j in range(i+1, n):
        if arr[j] - arr[i] < min_dif:
            min_dif = arr[j] - arr[i]

print(min_dif)