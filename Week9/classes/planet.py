class Planet:

    def __init__(self, name):
        self.name = name
        self.humans = []
        self.robots = []


    def add(self,type,obj):
        if type == 'human':
            self.humans.append(obj)
        elif type == 'robot':
            self.robots.append(obj)

    def remove(self, type):
        if type == 'human':
            self.humans.remove(type)
        elif type == 'robot':
            self.robots.remove(type)

    def __str__(self):
        return "Name: '" + self.name + "' Humans: " + f'{self.humans}' + " Robots: " + f'{self.robots}'


