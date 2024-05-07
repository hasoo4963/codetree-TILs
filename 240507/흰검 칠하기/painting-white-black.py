class Tile:
    def __init__(self):
        self.blackCount = 0
        self.whiteCount = 0
        self.lastColor = "Transparent"

def isCountEq2(arr, i):
    if arr[i].blackCount == 2 and arr[i].whiteCount == 2:
        return True
    else:
        return False

def Grey(arr, i):
    arr[i].lastColor = "Grey"

def move(arr, now_pos, x, direction):
    if direction == "L":
        temp = now_pos - x
        for i in range(temp + 1, now_pos + 1):

            arr[i].whiteCount += 1

            if isCountEq2(arr, i):
                Grey(arr, i)
                continue

            arr[i].lastColor = "White"
    elif direction == "R":
        temp = now_pos + x
        for i in range(now_pos, temp):
            
            arr[i].blackCount += 1


            if isCountEq2(arr, i):
                Grey(arr, i)
                continue

            arr[i].lastColor = "Black"

tiles = []
for _ in range(200005):
    tiles.append(Tile())

now_pos = 100000
n = int(input())
for _ in range(n):
    x, direction = input().split()
    x = int(x)

    if direction == "L":
        move(tiles, now_pos, x, "L")
        now_pos = now_pos - x + 1
    elif direction == "R":
        move(tiles, now_pos, x, "R")
        now_pos = now_pos + x - 1

sumGrey = 0
sumWhite = 0
sumBlack = 0
for elem in tiles:
    if elem.lastColor == "Grey":
        sumGrey += 1
    elif elem.lastColor == "White":
        sumWhite += 1
    elif elem.lastColor == "Black":
        sumBlack += 1
print(sumWhite, sumBlack, sumGrey)