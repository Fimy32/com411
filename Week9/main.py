from Week9.classes import robot as robotclass, human as humanclass, planet as planetclass, universe as universeclass
import random
human = humanclass.Human()
human.display()
robot = robotclass.Robot()
robot.display()


for i in range(20):
    robot.grow()
    robot.eat(2)
    if robot.move(i):
        print("Moving",i,"Steps")
    else:
        print("Not enough energy to move",i)
    print(robot, "\n\n")

planet = planetclass.Planet("Ultimate Planet")
for i in range(20):
    if random.randint(0,2) == 1:
        planet.add("human",human)
    if random.randint(0,2) == 1:
        planet.add("robot",robot)

#print(planet)
print(planet.name)
for human in planet.inhabitants["humans"]:
    print(human)
for robot in planet.inhabitants["robots"]:
    print(robot)

universe = universeclass.Universe()
for i in range(20):
    universe.generate()



universe.show_population("human")
universe.show_population("robots")
universe.show_population("both")