arr = list(map(int,input().split()))
new_arr = []

for elem in arr:
    if elem == 0:
        break;
    else:
        new_arr.append(elem)

n = len(new_arr)
sum_val = sum(new_arr)
avg = sum_val / n

print(f"{sum_val} {avg:.1f}")