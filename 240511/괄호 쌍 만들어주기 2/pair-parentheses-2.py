S = input()

answer = 0
for i in range(len(S)):
    for j in range(i+2, len(S)-1):
        if S[i] == '(' and S[i+1] == '(' and S[j] == ')' and S[j+1] == ')':
            answer += 1

print(answer)