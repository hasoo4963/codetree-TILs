R,C = map(int, input().split())
arr_2d = [
    list(input().split())
    for _ in range(R)
]

answer = 0

x, y = 0, 0

for i in range(1, R-1):
    for j in range(1, C-1):
        for k in range(i+1, R-1):
            for l in range(j+1, C-1):
                if arr_2d[0][0] != arr_2d[i][j] and arr_2d[i][j] != arr_2d[k][l] and arr_2d[k][l] != arr_2d[R-1][C-1]:
                    answer += 1

print(answer)