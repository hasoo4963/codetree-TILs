directionStr = input()
n = len(directionStr)

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

x, y = 0, 0
t = 0
flag = 0

now_pos = 0

for i in range(n):
    direction = directionStr[i]

    if direction == 'F':
        x, y = x + dxs[now_pos], y + dys[now_pos]
        t += 1
    elif direction == 'R':
        now_pos = (now_pos + 1) % 4
        t += 1
    else:
        now_pos = (now_pos + 4) % 4
        t += 1

    if x == 0 and y == 0:
        flag = 1
        break

if flag == 0:
    print(-1)
else:
    print(t)