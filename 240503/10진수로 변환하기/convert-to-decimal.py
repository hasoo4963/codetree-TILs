binary = list(map(int, input()))
num = 0

j = 0
for i in range(len(binary) - 1,-1,-1):
    num += (2**j) * binary[i]
    j += 1

print(num)