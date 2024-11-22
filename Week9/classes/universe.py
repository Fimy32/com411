from Week9.classes.planet import Planet
import random
from Week9.classes.human import Human
from Week9.classes.robot import Robot
import matplotlib.pyplot as plt

class Universe:
    def __init__(self):
        self.planets = []

    def generate(self):
        temp = Planet("Cool Planet" + str(random.randint(0,1111)))
        for i in range(random.randint(0,10)):
            temp.add("human",Human())
        for i in range(random.randint(0,10)):
            temp.add("robot",Robot())
        self.planets.append(temp)

    def show_population(self, selection):
        if selection == "human":
            x = []
            y = []
            for i in range(len(self.planets)):
                x.append(len(self.planets[i].inhabitants["humans"]))
                y.append(self.planets[i].name)
        elif selection == "robots":
            x = []
            y = []
            for i in range(len(self.planets)):
                x.append(len(self.planets[i].inhabitants["robots"]))
                y.append(self.planets[i].name)
        else:
            x = []
            y = []
            for i in range(len(self.planets)):
                x.append(len(self.planets[i].inhabitants["humans"]))
                x.append(len(self.planets[i].inhabitants["robots"]))
                y.append(self.planets[i].name)
        plt.bar(y,x)
        plt.xticks(rotation=45)
        plt.show()

