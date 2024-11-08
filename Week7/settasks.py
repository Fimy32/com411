#Simple Sets

def observed():
    observations = {"Car","Sky Scraper", "Bike", "House"}
    return observations


def run_task1():
    print(observed())


run_task1()


#Sets with duplicates

def observed_items():
    observations = set()
    for i in range(7):
        observations.add(input("Enter Observation"))
    return observations

def run_task2():
    print(observed_items())

run_task2()