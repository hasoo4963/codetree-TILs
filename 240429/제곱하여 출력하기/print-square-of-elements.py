n = int(input())
a = input().split()
new_arr = []
for i in range (0, n):
    new_arr.append(int(a[i])**2)

for i in range (0, n):
    print(new_arr[i], end = " ")