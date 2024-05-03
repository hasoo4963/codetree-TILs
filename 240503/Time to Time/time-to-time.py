arr = input().split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
d = int(arr[3])

start_time = 60*a + b
finish_time = 60*c + d

print(finish_time - start_time)