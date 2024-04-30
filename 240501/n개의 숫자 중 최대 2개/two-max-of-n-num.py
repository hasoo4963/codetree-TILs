n = int(input())
arr = list(map(int,input().split()))

def shift_vac_rec(arr, i, key):
    if i == 0:
        arr[0] = key
        return
    
    if arr[i-1] >= key:
        arr[i] = key
        return
    else:
        arr[i] = arr[i-1]
        shift_vac_rec(arr, i-1, key)

for i in range(1, n):
    key = arr[i]
    shift_vac_rec(arr, i, key)

print(arr[0], arr[1])