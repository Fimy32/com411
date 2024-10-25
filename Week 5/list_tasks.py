#Simple List

def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps

def run_task1():
    print(directions())

if __name__ == "__main__":
    run_task1()



#Simple list with varying data types

def movements():
    path = ["Move forward", 10, "Move backward", 5, "Move left", 3, "Move right", 1]
    return path

def run_task2():
    print("Moving...")
    temp_movements = movements()
    for i in range(1, len(temp_movements) - 1,2):
        print(temp_movements[i],"for",temp_movements[i+1],"steps")

if __name__ == "__main__":
    run_task2()

#Iterating a list

def menu():
    print("Please select a direction:")
    temp_directions = directions()
    for i in range(len(temp_directions)):
        print(i,":",temp_directions[i])
    print("")

def run_task3():
    menu()

if __name__ == "__main__":
    run_task3()


#populating a list

def menu_and_input():
    menu()
    user_direction = int(input(" "))
    return directions()[user_direction]

def run_task4():
    print("Working out escape route...")
    route = []
    for i in range(1,5):
        route.append(menu_and_input())
    print("Escape route:",route)

if __name__ == "__main__":
    run_task4()

