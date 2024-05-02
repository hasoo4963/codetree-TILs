def isEqual(arr1, arr2, n):
    for i in range(n):
        if arr1[i] != arr2[i]:
            return False
    return True

arr1 = list(input())
arr2 = list(input())

arr1.sort()
arr2.sort()

if len(arr1) != len(arr2):
    print("No")
else:
    n = len(arr1)
    if isEqual(arr1, arr2, n):
        print("Yes")
    else:
        print("No")