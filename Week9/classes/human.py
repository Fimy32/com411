class Human:
    def __init__(self):
        self.MAX_ENERGY = 100
        self.name = "Human"
        self.age = 0
        self.energy = self.MAX_ENERGY

    def display(self):
        print("I am",self.name)

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy = self.energy + amount
        if self.energy > self.MAX_ENERGY:
            self.energy = self.MAX_ENERGY

    def move(self, distance):
        if distance > self.energy:
            return False
        else:
            self.energy -= distance
            return True

    def __str__(self):
        return f'{self.name},{self.age},{self.energy}'

    def __repr__(self):
        return self.name,self.age,self.energy