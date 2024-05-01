N = int(input())
word = []
for i in range(N):
    word.append(input())

word.sort()
for elem in word:
    print(elem)