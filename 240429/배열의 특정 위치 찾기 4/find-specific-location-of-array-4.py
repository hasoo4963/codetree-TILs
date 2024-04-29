arr = list(map(int, input().split()))
new_arr = []

sum = 0
count = 0

for elem in arr:
    if elem == 0:
        break;
    elif elem % 2 == 0:
        sum += elem
        count += 1

print(f"{count} {sum}")