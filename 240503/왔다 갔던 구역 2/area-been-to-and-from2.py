def move(arr, now_pos , x, direction):
    if direction == "L":
        for i in range(x, now_pos):
            arr[i] += 1
        return x
    elif direction == "R":
        for i in range(now_pos, x):
            arr[i] += 1
        return x


n = int(input())
position = [0] * 2000

now_pos = 1000
for i in range(n):
    x, direction = map(str,input().split())
    x = int(x)

    if direction == "L":
        x = now_pos - x
    elif direction == "R":
        x = now_pos + x

    now_pos = move(position, now_pos, x, direction)
    
sum = 0
for elem in position:
    if elem >= 2:
        sum += 1
print(sum)