n = int(input())
arr1 = list(map(int, input().split()))

arr1.sort()
print(*arr1)

arr1.sort(reverse=True)
print(*arr1)