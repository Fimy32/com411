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


# #While loop with a counter
#
# obstacle_num = int(input("How many obstacles should I avoid?"))
#
# current_obstacle = 0
#
# while current_obstacle < obstacle_num:
#
#     current_obstacle = current_obstacle + 1
#
#     print("Avoiding...Done!", current_obstacle,"avoided.")
#


# #While loop with ASCII art
#
# bars_to_charge = int(input("How many bars do you want to charge?"))
#
# print(bars_to_charge,"\n")
#
# bars_charged = 0
#
# while bars_charged < bars_to_charge:
#
#     bars_charged += 1
#
#     print("Charging:", "[=]" * bars_charged)
#
# print("The battery is fully charged.")


#While loop reading users input

phrase = str(input("Enter a phrase:"))

print(phrase,"\n")

phrase_number = len(phrase)

counter = 0

while counter < phrase_number:

    counter += 1

    print("Hi", end=" ")

