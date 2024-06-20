class Building:
    def __init__(self, numberOfFloors: int, buildingType: str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):      # self-первый участник, other - второй участник
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


h1 = Building('apartment house', 18)
h2 = Building('apartment house', 18)
