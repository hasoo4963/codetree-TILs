class Address:
    def __init__(self, name, street, location):
        self.name = name
        self.street = street
        self.location = location
    def print(self):
        print(f"name {self.name}\naddr {self.street}\ncity {self.location}")

N = int(input())
addressList = []
for i in range(N):
    name, street, location = tuple(map(str, input().split()))
    adr = Address(name, street, location)
    addressList.append(adr)

name_list = [ addressList[i].name for i in range(len(addressList)) ]
name_list.sort()

for elem in addressList:
    if elem.name == name_list[len(name_list) - 1]:
        elem.print()