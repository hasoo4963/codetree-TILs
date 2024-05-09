S = list(input())
length = len(S)

sum = 0

for i in range(length):
    if S[i] != "1":
        S[i] = '1'
        break

for i in range(length):
    sum = sum + (2**(length - 1 - i))*int(S[i])

print(sum)