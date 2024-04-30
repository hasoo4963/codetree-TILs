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

def isDuplicate(arr, key):
    count = 0
    for elem in arr:
        if elem == key:
            count += 1
    
    if count != 1:
        return True
    else:
        return False

for i in range(n):
    max_val = arr[i]
    if isDuplicate(arr, max_val) == False:
        print(max_val)
        break

    if i == n-1:
        print(-1)