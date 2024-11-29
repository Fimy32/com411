from planet import Planet
import random
import matplotlib.pyplot as plt

class Universe:
    def __init__(self):
        self.planet_list = []
        for i in range(random.randint(1, 20)):
            self.planet_list.append(Planet())

    def show_population(self):
        for i in range(len(self.planet_list)):
            print("Planet", str(random.randint(1,99999999)),self.planet_list[i].return_population())

    def show_population_grapth(self, selection):
        if selection == "human":
            x = []
            y = []
            for i in range(len(self.planet_list)):
                x.append(self.planet_list[i].return_population_tuple()[0])
                y.append("P" + str(i))
        elif selection == "robots":
            x = []
            y = []
            for i in range(len(self.planet_list)):
                x.append(self.planet_list[i].return_population_tuple()[1])
                y.append("P" + str(i))
        else:
            x = []
            y = []
            for i in range(len(self.planet_list)):
                x.append(self.planet_list[i].return_population_tuple()[1] + self.planet_list[i].return_population_tuple()[0])
                y.append("P" + str(i))
        plt.bar(y,x)
        plt.xticks(rotation=45)
        plt.show()