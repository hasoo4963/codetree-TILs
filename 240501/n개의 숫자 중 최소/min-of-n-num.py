n = int(input())
arr = list(map(int, input().split()))

min_val = arr[0]
for elem in arr[1:]:
    if min_val > elem:
        min_val = elem

count = 0
for elem in arr:
    if elem == min_val:
        count += 1

print(min_val, count)