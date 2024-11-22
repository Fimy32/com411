class Human:
    def __init__(self):
        self.MAX_ENERGY = 100
        self.name = "Human"
        self.age = 0
        self.energy = self.MAX_ENERGY

    def display(self):
        print("I am",self.name)
