def calculate(num_of_days, m1, d1):
    sum = 0
    for i in range(m1):
        sum += num_of_days[i]
    sum += d1
    return sum

m1, d1, m2, d2 = map(int, input().split())
day = input()
idx = 0

num_of_days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
date = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for i in range(len(date)):
    if day == date[i]:
       idx = i
       break 

startDate = calculate(num_of_days, m1, d1 + idx)
endDate = calculate(num_of_days, m2, d2)

diff = (endDate - startDate) // 7
print(diff + 1)