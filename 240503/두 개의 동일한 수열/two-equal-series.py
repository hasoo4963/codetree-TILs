def isEqual(arr1, arr2, N):
    idx = 0
    while idx < N:
        if arr1[idx] != arr2[idx]:
            return False
        idx += 1
    return True

n = int(input())
arr1 = input().split()
arr2 = input().split()

for i in range(n):
    arr1[i] = int(arr1[i])
    arr2[i] = int(arr2[i])

arr1.sort()
arr2.sort()
if isEqual(arr1, arr2, n):
    print("Yes")
else:
    print("No")