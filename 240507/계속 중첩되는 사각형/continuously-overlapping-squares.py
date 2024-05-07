def draw(arr, color, x1, y1, x2, y2):
    if color == "Blue":
        for i in range(x1, x2):
            for j in range(y1, y2):
                arr[i][j] = 1
    elif color == "Red":
        for i in range(x1, x2):
            for j in range(y1,y2):
                arr[i][j] = 2

arr_2d = [
    [0] * 405
    for _ in range(405)
]
n = int(input())
for i in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100

    if i % 2 == 0:
        draw(arr_2d, "Red", x1, y1, x2, y2)
    else:
        draw(arr_2d, "Blue", x1, y1, x2, y2)

sum = 0
for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
        if arr_2d[i][j] == 1:
            sum += 1
print(sum)