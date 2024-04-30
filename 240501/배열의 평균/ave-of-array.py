arr_2d = [ list(map(int, input().split())) for i in range(2) ]

avg_width = []
avg_verical = []
avg = 0

for i in range(2):
    sum_val = sum(arr_2d[i])
    avg_width.append(sum_val / 4)

for j in range(4):
    sum_val = 0
    for i in range(2):
        sum_val += arr_2d[i][j]
    avg_verical.append(sum_val / 2)

sum_val = 0
for i in range(2):
    for j in range(4):
        sum_val += arr_2d[i][j]
avg = sum_val / 8

for elem in avg_width:
    print(f"{elem:.1f}", end = " ")

print()

for elem in avg_verical:
    print(f"{elem:.1f}", end = " ")

print()

print(f"{avg:.1f}")