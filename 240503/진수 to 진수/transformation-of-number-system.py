a, b = map(int, input().split())
n = list(map(int, input()))

decimalPoint = 0
j = 0
for i in range(len(n) - 1, -1, -1):
    decimalPoint += (a**j) * n[i]
    j += 1

arr = []
while decimalPoint > 0:
    arr.append(decimalPoint % b)
    decimalPoint //= b

print(*arr[::-1], sep="")