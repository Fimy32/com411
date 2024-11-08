# #Simple Sets
#
# def observed():
#     observations = {"Car","Sky Scraper", "Bike", "House"}
#     return observations
#
#
# def run_task1():
#     print(observed())
#
#
# run_task1()
#
#
# #Sets with duplicates
#
# def observed_items():
#     observations = []
#     for i in range(7):
#         observations.append(input("Enter Observation"))
#     return observations
#
# def run_task2():
#     print("Counting Observations")
#     observeditems = observed_items()
#     observed_set = set()
#     for element in observeditems:
#         observed_set.add((element, observeditems.count(element)))
#     print(observed_set)
#
# run_task2()


# #Removing From A set
#
# def observed_items():
#     observations = []
#     for i in range(5):
#         observations.append(input("Enter Observation"))
#     return observations
#
# def remove_observations(observations):
#     while input("Would you like to remove observations? [y/n]") == "y":
#         observations.remove(input("Enter Observation"))
#     return observations
#
# def run_task3():
#     observeditems = remove_observations(observed_items())
#     observed_set = set()
#     for element in observeditems:
#         observed_set.add((element, observeditems.count(element)))
#     print(observed_set)
#
# run_task3()

