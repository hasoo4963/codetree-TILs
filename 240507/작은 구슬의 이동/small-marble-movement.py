# n = 5
# x, y = 1, 2
# dir_num = 2

# dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]


# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < n


# while keep_moving():
#     nx, ny = x + dxs[dir_num], y + dys[dir_num]
#     if not in_range(nx, ny):  # check whether position is out of grid
#         dir_num = 3 - dir_num # change direction
    
#     # move
#     x, y = x + dxs[dir_num], y + dys[dir_num]



n, t = map(int, input().split())
r, c, d = input().split()

def isInRange(dx, dy, n):
    if 0 <= dx < n and 0 <= dy < n:
        return True
    else:
        return False    

mapper = {
    'U' : 0,
    'D' : 3,
    'R' : 1,
    'L' : 2
}

dxs, dys = [-1,0,0,1], [0,1,-1,0]

arr_2d = [ 
    [0] * n
    for _ in range(n)
]

x = int(r) - 1
y = int(c) - 1
dir_num = mapper[d]
while t != 0:
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not isInRange(nx, ny, n):
        dir_num = 3 - dir_num
        t -= 1
        continue
    
    x = nx
    y = ny
    t -= 1

print(x + 1, y + 1)