def draw(arr_2d, x1, y1, x2, y2, value):
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr_2d[i][j] = value

def isComplete(arr_2d):
    for i in range(len(arr_2d)):
        for j in range(len(arr_2d[i])):
            if arr_2d[i][j] == 1:
                return False
    return True

first_x1, first_y1, first_x2, first_y2 = map(lambda x: int(x) + 1000, input().split())
second_x1, second_y1, second_x2, second_y2 = map(lambda x: int(x) + 1000, input().split())
arr_2d = [
    [0] * 2002
    for _ in range(2002)
]

draw(arr_2d, first_x1, first_y1, first_x2, first_y2, 1)
draw(arr_2d, second_x1, second_y1, second_x2, second_y2, 2)

if isComplete(arr_2d):
    print(0)
else:
    print((first_x2 - first_x1) * (first_y2-first_y1))