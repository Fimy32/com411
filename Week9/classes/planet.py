from Week9.classes.human import Human
from Week9.classes.robot import Robot

class Planet:

    def __init__(self, name):
        self.name = name
        self.inhabitants = {
        "humans" : [],
        "robots" : []
        }


    def add(self,type,obj):
        if type == 'human':
            self.inhabitants["humans"].append(obj)
        elif type == 'robot':
            self.inhabitants["robots"].append(obj)

    def remove(self, type):
        if type == 'human':
            self.inhabitants["humans"].remove(type)
        elif type == 'robot':
            self.inhabitants["robots"].remove(type)

    def __str__(self):
        return "Name: '" + self.name + "' Humans: " + f'{self.inhabitants}'


