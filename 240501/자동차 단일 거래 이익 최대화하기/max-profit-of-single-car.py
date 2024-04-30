n = int(input())
arr = list(map(int, input().split()))
income_table = []

def caculate_max_income(arr, key):
    if len(arr) == 0:
        return

    max_val = max(arr)
    if (max_val - key > 0):
        income_table.append(max_val - key)
    else:
        income_table.append(0)
    
for i in range(n):
    current_price = arr[i]
    caculate_max_income(arr[i+1:], current_price)

if n == 1:
    print(0)
else:
    print(max(income_table))