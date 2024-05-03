arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

day_start = 11
hour_start = 11
miniute_start = 11

first_time = (60*24*day_start) + (60*hour_start) + miniute_start
last_time = (60*24*a) + (60*b) + c

print(last_time - first_time)