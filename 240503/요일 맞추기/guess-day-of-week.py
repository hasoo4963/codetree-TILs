def calculate(num_of_days, m1, d1):
    sum = 0
    for i in range(m1):
        sum += num_of_days[i]
    sum += d1
    
    return sum

m1, d1, m2, d2 = map(int, input().split())
num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
date = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

start_day = calculate(num_of_days, m1, d1)
finish_day = calculate(num_of_days, m2, d2)

diff = (finish_day - start_day) % 7
print(date[diff])