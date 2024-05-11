import sys
N = int(input())

arr_2d = [
    list(map(int, input().split()))
    for _ in range(N)
]

min_val = sys.maxsize
for i in range(1, N-1):    # i번째 체크포인트를 건너뛰면
    temp = 0
    for j in range(N-1):
        if j+1 == i:        # 다음이 건너뛰는 포인트면 다다음과 연산필요
            temp += abs(arr_2d[j][0] - arr_2d[j+2][0]) + abs(arr_2d[j][1] - arr_2d[j+2][1])
        elif j == i:        # 지금이 건너뛰는 포인트면 아무 연산도 하지 않음
            continue
        else:
            temp += abs(arr_2d[j][0] - arr_2d[j+1][0]) + abs(arr_2d[j][1] - arr_2d[j+1][1])
    min_val = min(min_val, temp)

print(min_val)