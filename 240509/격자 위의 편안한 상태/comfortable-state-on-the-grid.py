N, M = map(int, input().split())
arr_2d = [
    [0] * N
    for _ in range(N)
]

dxs = [-1,1,0,0]
dys = [0,0,1,-1]

def isInRange(N, x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False

for _ in range(M):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    arr_2d[r][c] = 1

    cnt = 0

    for i in range(len(dxs)):
        tempR = r + dxs[i]
        tempS = c + dys[i]

        if isInRange(N, tempR, tempS):
            if arr_2d[tempR][tempS] == 1:
                cnt += 1
        else:
            continue

    if cnt == 3:
        print(1)
    else:
        print(0)