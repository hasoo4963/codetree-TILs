direction = list(map(str, input()))

x, y = 0, 0
N = len(direction)

dir_num = 0

dxs = [0,-1,0,1]
dys = [1,0,-1,0]

for i in range(N):
    if direction[i] == "L":
        dir_num = (dir_num + 1) % 4
    elif direction[i] == "R":
        dir_num = (dir_num - 1 + 3) % 4
    else:
        x = x + dxs[dir_num]
        y = y + dys[dir_num]
print(x, y)