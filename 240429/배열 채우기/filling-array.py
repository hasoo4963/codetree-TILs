arr = list(map(int, input().split()))
new_arr = []

for elem in arr:
    if elem == 0:
        break;
    else:
        new_arr.append(elem)

n = len(new_arr)
for i in range(n-1, -1, -1):
    print(new_arr[i], end=" ")