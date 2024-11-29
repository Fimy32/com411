from human import Human
from robot import Robot
import random

class Planet:
    def __init__(self,):
        self.inhabitant_list = []
        for i in range(random.randint(1,20)):
            self.inhabitant_list.append(Human("Human " + str(i)))
        for i in range(random.randint(1,20)):
            self.inhabitant_list.append(Robot("Robot " + str(i)))

    def add_inhabitant(self, inhabitant):
        self.inhabitant_list.append(inhabitant)

    def remove_inhabitant(self, name):
        self.inhabitant_list.remove(name)

    def return_population(self):
        counter = []
        for i in range(len(self.inhabitant_list)):
            counter.append(isinstance(self.inhabitant_list[i],Human))
        total_humans = 0
        total_robots = 0
        for i in range(len(counter)):
            if counter[i]:
                total_humans += 1
            else:
                total_robots += 1

        return ("Humans:", total_humans), ("Robots:", total_robots)

    def return_population_tuple(self):
        counter = []
        for i in range(len(self.inhabitant_list)):
            counter.append(isinstance(self.inhabitant_list[i],Human))
        total_humans = 0
        total_robots = 0
        for i in range(len(counter)):
            if counter[i]:
                total_humans += 1
            else:
                total_robots += 1

        return total_humans, total_robots