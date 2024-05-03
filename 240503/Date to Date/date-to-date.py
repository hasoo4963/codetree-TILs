def caculate(numDay, m1, d1):
    sum = 0

    for i in range(m1):
        sum += numDay[i]
    sum += d1

    return sum

arr = input().split()
m1 = int(arr[0])
d1 = int(arr[1])
m2 = int(arr[2])
d2 = int(arr[3])

numDay = [0,31,28,31,30,31,30,31,31,30,31,30,31]

first = caculate(numDay, m1, d1)
second = caculate(numDay, m2, d2)

print(second - first + 1)