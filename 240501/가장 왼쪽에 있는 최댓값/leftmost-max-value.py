n = int(input())
arr = list(map(int, input().split()))
idx_arr = []

def find_max(arr):
    length = len(arr)
    max_val = max(arr)

    for i in range(length):
        if max_val == arr[i]:
            idx_arr.append(i + 1)
            return i

while 1:
    temp_idx = find_max(arr)

    if temp_idx == 0:
        break

    arr = arr[:temp_idx]

print(*idx_arr)