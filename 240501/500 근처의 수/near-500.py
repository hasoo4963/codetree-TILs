arr = list(map(int, input().split()))
under_500_idx = 0
upper_500_idx = 0

for i in range(len(arr)):
    if (arr[i] < 500):
        under_500_idx = i
    else:
        upper_500_idx = i

for i in range(len(arr)):
    if (arr[i] < 500):
        if (arr[i] > arr[under_500_idx]):
            under_500_idx = i
    else:
        if (arr[i] < arr[upper_500_idx]):
            upper_500_idx = i

print(arr[under_500_idx], arr[upper_500_idx])