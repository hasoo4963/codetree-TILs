n = int(input())
arr = []

arr.append(1)
arr.append(n)

while 1:
    arr.append(arr[-1] + arr[-2])
    n = len(arr)
    if(arr[n-1] >= 100):
        break;

print(*arr)