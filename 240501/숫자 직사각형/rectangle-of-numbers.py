arr = list(map(int, input().split()))
n = arr[0]
m = arr[1]

arr_2d = [ 
    [ 0 for _ in range(m) ]
    for _ in range(n)
 ]

num = 1

for i in range(n):
    for j in range(m):
        arr_2d[i][j] = num
        num += 1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()