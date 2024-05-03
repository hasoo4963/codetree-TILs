def draw(arr_2d, x1, y1, x2, y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr_2d[i][j] = 1

N = int(input())

arr_2d = [
    [0] * 201
    for _ in range(201)
]

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100

    draw(arr_2d, x1, y1, x2, y2)

sum = 0
for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
        if arr_2d[i][j] == 1:
            sum += 1
print(sum)