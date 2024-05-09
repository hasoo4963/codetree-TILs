n, m = map(int, input().split())
arr_2d = [
    [""] * m
    for _ in range(n)
]

def isInRange(n, m, x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
x, y = 0, 0
now_pos = 0

start_ascii = 65

arr_2d[x][y] = chr(start_ascii)
for _ in range(1, n*m):
    start_ascii += 1
    if start_ascii > 90:
        start_ascii = 65

    dx, dy = x + dxs[now_pos], y + dys[now_pos]

    if not isInRange(n, m, dx, dy) or arr_2d[dx][dy] != "":
        now_pos = (now_pos + 1) % 4

    x = x + dxs[now_pos]
    y = y + dys[now_pos]
    arr_2d[x][y] = chr(start_ascii)

for elem in arr_2d:
    print(*elem)