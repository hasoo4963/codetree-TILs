n = int(input())
# a = input().split()
a = list(map(int, input().split()))

#new_arr = []
#for i in range (0, n):
#    new_arr.append(int(a[i])**2)

new_arr = [ elem**2 for elem in a ]

for elem in new_arr:
    print(elem, end = " ")