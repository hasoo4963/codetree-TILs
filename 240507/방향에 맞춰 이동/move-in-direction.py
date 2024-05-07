dxs, dys = [1,0,-1,0], [0,-1,0,1]
x, y = 0, 0
N = int(input())

mapping = {
    'N' : 3,
    'E' : 0,
    'S' : 1,
    'W' : 2
}

for _ in range(N):
    direction, count = input().split()
    count = int(count)
    dir_num = mapping[direction]
    
    x, y = x + dxs[dir_num] * count, y + dys[dir_num] * count

print(x, y)