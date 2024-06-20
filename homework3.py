from for3 import h1, h2 # я захотела применить знания по недавней теме импортирования кода и создала ещё один документ с
# типом здания и этажом который потом импортировала сюда

class Building:
    def __init__(self, numberOfFloors: int, buildingType: str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eg__(self, other): # self-первый участник, other - второй участник
         return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


print(print(h1 == h2)
