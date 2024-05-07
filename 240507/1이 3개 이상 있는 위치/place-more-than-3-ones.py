# a = [[0, 0, 0, 1, 0],
#      [0, 1, 1, 1, 0],
#      [0, 0, 0, 0, 1],
#      [1, 0, 1, 1, 1],
#      [1, 0, 1, 1, 0]]

# x, y = 2, 4

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def isExist1(arr_2d, x, y):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny, n) and arr_2d[nx][ny] == 1:
        # if 문의 범위 체크 시에는 조건 중에 젤 앞에 적어야 한다.
            cnt += 1
    return cnt




n = int(input())
arr_2d = []
for i in range(n):
    arr_2d.append(list(map(int, input().split())))

cnt = 0

for i in range(n):
    for j in range(n):
        if isExist1(arr_2d, i , j) >= 3:
            cnt += 1

print(cnt)


# for i in range(len(arr_2d)):
#     for j in range(len(arr_2d[i])):
#         print(arr_2d[i][j])