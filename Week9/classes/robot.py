class Robot:
    def __init__(self):
        self.MAX_ENERGY = 100
        self.name = "Human"
        self.age = 0
        self.energy = 0

    def display(self):
        print("I am",self.name)

    def __str__(self):
        return self.name,self.age,self.energy

    def __repr__(self):
        return self.name,self.age,self.energy