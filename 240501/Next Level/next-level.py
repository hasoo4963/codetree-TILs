class Object:
    def __init__(self, id = "codetree", level = "10"):
        self.id = id
        self.level = level

arr = list(input().split())

obj1 = Object()

print(f"user {obj1.id} lv {obj1.level}")

obj1.id = arr[0]
obj1.level = arr[1]

print(f"user {obj1.id} lv {obj1.level}")