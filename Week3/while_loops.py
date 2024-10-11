# #Simple While Loop
#
# apples = int(input("How many apples should I remove?"))
#
# print(apples)
#
# removed_apples = 0
#
# while apples > removed_apples:
#     print("Remove Apple")
#     removed_apples += 1

#While loop with a counter

obstacle_num = int(input("How many obstacles should I avoid?"))

current_obstacle = 0

while current_obstacle < obstacle_num:

    current_obstacle = current_obstacle + 1

    print("Avoiding...Done!", current_obstacle,"avoided.")