# #Simple nested for loops
#
# rows = int(input("How many rows should I have?"))
#
# columns = int(input("How many columns should I have?"))
#
# for i in range(columns):
#     print("\n")
#     for i in range(rows):
#         print(">:[", end=" ")


#Nested Loops and Decisions

sequence = str(input("Please enter sequence"))

marker = str(input("Please enter marker"))

distance = -2

marker_number = 0

found_marker = False

for letter in sequence:

    if letter == marker:
        marker_number += 1

    for i in range(len(sequence) - 1,0,-1):

        distance += 1
        if (sequence[i] == marker):
            break

print("The distance between markers is",distance)





