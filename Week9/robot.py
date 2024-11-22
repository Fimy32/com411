class Robot:
    def __init__(self):
        self.MAX_ENERGY = 100
        self.name = "Human"
        self.age = 0
        self.energy = 0

    def display(self):
        print("I am",self.name)