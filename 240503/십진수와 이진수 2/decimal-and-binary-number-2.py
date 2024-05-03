N = list(map(int, input()))
decimalPoint = 0
j = 0

for i in range(len(N)-1,-1,-1):
    decimalPoint += (2**j) * N[i]
    j += 1

decimalPoint *= 17

binaryArr = []
while decimalPoint > 0:
    binaryArr.append(decimalPoint % 2)
    decimalPoint //= 2

print(*binaryArr[::-1], sep="")