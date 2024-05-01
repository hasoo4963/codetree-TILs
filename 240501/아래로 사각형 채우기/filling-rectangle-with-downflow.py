n = int(input())
arr_2d = [
    [ 0 for i in range(n) ]
    for i in range(n)
]

num = 1
for i in range(n):
    for j in range(n):
        temp = n*j
        arr_2d[i][j] = num + temp
    num += 1

for i in range(n):
    for j in range(n):
        print(arr_2d[i][j], end=" ")
    print()