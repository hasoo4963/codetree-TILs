a = int(input())
arr = []
count = 0
i = 1

while count != 2:
    temp = a * i
    if temp % 5 == 0:
        count += 1
        arr.append(temp)
    else:
        arr.append(temp)
    i += 1

print(*arr)