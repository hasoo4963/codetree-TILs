S = input()

answer = 0
for i in range(len(S)):
    for j in range(i+1, len(S)):
        if S[i] == "(" and S[j] == ")":
            answer += 1

print(answer)