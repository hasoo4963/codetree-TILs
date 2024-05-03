N, B = map(int, input().split())
arr = []
while N > 0:
    arr.append(N % B)
    N //= B

print(*arr[::-1], sep="")