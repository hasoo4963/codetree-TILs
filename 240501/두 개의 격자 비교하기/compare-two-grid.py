arr = list(map(int, input().split()))
n = arr[0]
m = arr[1]

arr_2d_1 = [ list(map(int, input().split())) for i in range(n) ]
arr_2d_2 = [ list(map(int, input().split())) for i in range(n) ]

for i in range(n):
    for j in range(m):
        if(arr_2d_1[i][j] == arr_2d_2[i][j]):
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()