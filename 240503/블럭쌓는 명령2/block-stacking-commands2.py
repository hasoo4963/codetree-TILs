N, K = map(int,input().split())

block = [0]*(N+1)
for i in range(K):
    first, last = map(int, input().split())
    for i in range(first, last+1):
        block[i] += 1
    
max = 0
for elem in block:
    if elem > max:
        max = elem
print(max)