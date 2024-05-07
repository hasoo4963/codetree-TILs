x, y = 0, 0
N = int(input())
t = 0

dxs = [1,-1,0,0]
dys = [0,0,-1,1]

Mapping = {
    'E' : 0,
    'W' : 1,
    'S' : 2,
    'N' : 3
}

flag_bit = 0
for _ in range(N):
    direction, count = input().split()
    count = int(count)

    dir_num = Mapping[direction]

    for i in range(count):
        x = x + dxs[dir_num]
        y = y + dys[dir_num]

        t += 1

        if x == 0 and y == 0:
            flag_bit = 1
            break

    if flag_bit == 1:
        break

if flag_bit == 1:
    print(t)
else:
    print(-1)