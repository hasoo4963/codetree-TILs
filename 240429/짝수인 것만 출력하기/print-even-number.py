n = int(input())
arr = list(map(int,input().split()))
new_arr = []

for elem in arr:
    if elem % 2 == 0:
        new_arr.append(elem)
print(*new_arr)