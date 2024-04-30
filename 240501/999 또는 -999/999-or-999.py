arr = list(map(int, input().split()))
new_arr = []

for i in range(100):
    temp = arr[i]
    if temp == 999 or temp == -999:
        break;
    else:
        new_arr.append(temp)

min_val = min(new_arr)
max_val = max(new_arr)

print(max_val, min_val)