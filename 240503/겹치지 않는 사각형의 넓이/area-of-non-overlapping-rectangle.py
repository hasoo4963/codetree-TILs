def draw(arr_2d, x1, y1, x2, y2, value):
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr_2d[i][j] = value

Ax1, Ay1, Ax2, Ay2 = map(int,input().split())
Bx1, By1, Bx2, By2 = map(int,input().split())
Mx1, My1, Mx2, My2 = map(int,input().split())

arr_2d = [
    [0] * 2001
    for _ in range(2001)
]

draw(arr_2d, Ax1 + 1000, Ay1 + 1000, Ax2 + 1000, Ay2 + 1000, 1)
draw(arr_2d, Bx1 + 1000, By1 + 1000, Bx2 + 1000, By2 + 1000, 1)
draw(arr_2d, Mx1 + 1000, My1 + 1000, Mx2 + 1000, My2 + 1000, 2)

sum = 0
for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
        if arr_2d[i][j] == 1:
            sum += 1
print(sum)