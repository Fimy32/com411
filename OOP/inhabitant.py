class Inhabitant:

    MAX_ENERGY = 100

    def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy

    def __str__(self):
        return str(self.name) + " " +  str(self.age) + " " + str(self.energy)

    def __repr__(self):
        return self.__str__()

    def eat(self, amount):
        pass

    def grow(self,):
        pass

    def move(self, distance):
        pass

