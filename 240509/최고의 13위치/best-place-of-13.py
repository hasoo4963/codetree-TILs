N = int(input())
arr_2d = [
    list(map(int, input().split()))
    for _ in range(N)
]

max_cnt = 0
for i in range(N):
    for j in range(N-2):
        max_cnt = max(max_cnt, arr_2d[i][j] + arr_2d[i][j+1] + arr_2d[i][j+2])

print(max_cnt)