userInput = input().split()
a = int(userInput[0])
b = int(userInput[1])

a += b
b += a
print(f"{a} {b}")