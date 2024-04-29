student_num = int(input())

count = 0
for i in range(student_num):
    arr = list(map(int,input().split()))
    if sum(arr) >= 240:
        print("pass")
        count += 1
    else:
        print("fail")
print(count)