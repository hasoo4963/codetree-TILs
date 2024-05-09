def isAll1(arr):
    for i in range(len(arr)):
        if arr[i] == "0":
            return False
    return True
# 요소가 전부 1인지 검사하는 코드

S = list(input())
length = len(S)

sum = 0

if length == 1:
    if S[0] == "1":
        S[0] = "0"
    else:
        S[0] = "1"
#length가 1인지 검사해 적절한 조치 취하기
else:
    if isAll1(S):
        S[length - 1] = "0"
    else:
        for i in range(length):
            if S[i] != "1":
                S[i] = '1'
                break
#length가 0은 아니지만 모두 1인경우에 0을 한군데에는 달아줘야함

for i in range(length):
    sum = sum + (2**(length - 1 - i))*int(S[i])

print(sum)