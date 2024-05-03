n = int(input())
block = [0] * 101

for i in range(n):
    first, last = map(int, input().split())
    for j in range(first, last + 1):
        block[j] += 1

print(max(block))