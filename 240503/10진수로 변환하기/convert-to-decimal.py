binary = list(map(int, input()))
num = 0

j = 0
for i in range(4,-1,-1):
    num += (2**j) * binary[i]
    j += 1

print(num)