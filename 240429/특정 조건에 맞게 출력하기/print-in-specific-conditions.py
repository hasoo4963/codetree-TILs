arr = list(map(int, input().split()))
new_arr = []

for elem in arr:
    if elem == 0:
        break;
    else:
        new_arr.append(elem)

for elem in new_arr:
    if elem % 2 == 1:
        print(elem + 3, end = " ")
    elif elem % 2 == 0:
        print(elem // 2, end = " ")