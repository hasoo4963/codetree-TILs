agents = []

class Agent:
    def __init__(self, codeName, score):
        self.codeName = codeName
        self.score = score

minScore = 101
minIdx = -1
for i in range(5):
    codeName, score = tuple(map(str, input().split()))
    score = int(score)

    if minScore > score:
        minScore = score
        minIdx = i

    agents.append(Agent(codeName, score))

print(agents[minIdx].codeName, agents[minIdx].score)