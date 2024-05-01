N = int(input())

class Data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather
    def print(self):
        print(self.date, self.day, self.weather)

dataArr = [
    Data(*map(str, input().split()))
    for _ in range(N)
]

dateArr = []
for i in range(N):
    if dataArr[i].weather == "Rain":
        dateArr.append(dataArr[i].date)
dateArr.sort()

for i in range(N):
    if dataArr[i].date == dateArr[0]:
        dataArr[i].print()