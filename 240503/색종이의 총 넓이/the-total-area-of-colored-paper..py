N = int(input())
arr_2d = [
    [0] * 205
    for _ in range(205)
]

for i in range(N):
    x1, y1 = map(lambda x: int(x)+100, input().split())

    for i in range(x1, x1+8):
        for j in range(y1, y1+8):
            arr_2d[i][j] = 1

sum = 0
for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
        if arr_2d[i][j] == 1:
            sum += 1
print(sum)