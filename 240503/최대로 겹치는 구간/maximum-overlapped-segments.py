n = int(input())
block = [0]*200

for i in range(n):
    x1, x2 = map(int, input().split())
    x1 += 100
    x2 += 100
    for i in range(x1, x2):
        block[i] += 1

max = 0
for elem in block:
    if max < elem:
        max = elem
print(max)