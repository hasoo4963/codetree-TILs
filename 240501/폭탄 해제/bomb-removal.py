class Object:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time

code, color, time = tuple(map(str, input().split()))
obj1 = Object(code, color, time)

print(f"code : {obj1.code}\ncolor : {obj1.color}\nsecond : {obj1.time}")