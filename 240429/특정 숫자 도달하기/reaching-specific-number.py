userInput = list(map(int, input().split()))
new_arr = []

for elem in userInput:
    if elem > 250:
        break
    else:
        new_arr.append(elem)

n = len(new_arr)

sum = 0
for elem in new_arr:
    sum += elem

avg = sum / n

print(f"{sum} {avg:.1f}")