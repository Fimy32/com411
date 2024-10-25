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