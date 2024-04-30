arr_2d = [ list(map(str, input().split())) for i in range(5) ]

for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
        print(arr_2d[i][j].upper(), end = " ")
    print()