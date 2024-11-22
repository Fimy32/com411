from planet import Planet
import random
from human import Human
from robot import Robot

class Universe:
    def __init__(self):
        self.planets = []

    def generate(self):
        temp = Planet("Cool Planet")
        for i in range(random.randint(0,10)):
            temp.add("human",Human())
        for i in range(random.randint(0,10)):
            temp.add("robot",Robot())
        self.planets.add(temp)
