n, m = map(int, input().split())
arr_2d = [
    [0] * m
    for _ in range(n)
]

def isInRange(n, m, x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False

dxs = [1,0,-1,0]
dys = [0,1,0,-1]

x, y = 0, 0
now_pos = 0

arr_2d[x][y] = 1

for i in range(2, n*m + 1):
    dx = x + dxs[now_pos]
    dy = y + dys[now_pos]

    if not isInRange(n, m, dx, dy) or arr_2d[dx][dy] != 0:
        now_pos = (now_pos + 1) % 4
    
    x = x + dxs[now_pos]
    y = y + dys[now_pos]

    arr_2d[x][y] = i

for elem in arr_2d:
    print(*elem)