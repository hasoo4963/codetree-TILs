class Body:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

bodyArr = []

for i in range(5):
    name, height, weight = input().split()
    bodyArr.append(Body(name, int(height), float(weight)))

bodyArr.sort(key = lambda x : x.name)

print("name")
for bd in bodyArr:
    print(f"{bd.name} {bd.height} {bd.weight:.1f}")


bodyArr.sort(key = lambda x : -x.height)

print()
print("height")
for bd in bodyArr:
    print(f"{bd.name} {bd.height} {bd.weight:.1f}")