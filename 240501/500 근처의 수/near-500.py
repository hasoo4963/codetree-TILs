arr = list(map(int, input().split()))
# under_500_idx = 0
# upper_500_idx = 0

# for i in range(len(arr)):
#     if (arr[i] < 500):
#         under_500_idx = i
#     else:
#         upper_500_idx = i

# for i in range(len(arr)):
#     if (arr[i] < 500):
#         if (arr[i] > arr[under_500_idx]):
#             under_500_idx = i
#     else:
#         if (arr[i] < arr[upper_500_idx]):
#             upper_500_idx = i

# print(arr[under_500_idx], arr[upper_500_idx])

max_val = 1
min_val = 1000

for i in range(10):
    if (max_val < arr[i] and arr[i] < 500):
        max_val = arr[i]
    elif (min_val > arr[i] and arr[i] > 500):
        min_val = arr[i]

print(max_val, min_val)