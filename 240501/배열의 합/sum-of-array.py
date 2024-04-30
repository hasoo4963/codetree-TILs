N = 4
arr_2d = []

# for i in range(N):
#     arr_1d = list(map(int, input().split()))
#     arr_2d.append(arr_1d)

arr_2d = [ list(map(int, input().split())) for i in range(N) ]

for i in range(N):
    sum_val = sum(arr_2d[i])
    print(sum_val)