from Week9.classes import robot as robotclass, human as humanclass

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

