# #Simple for loop
#
# mountain_count = int(input("How many mountains should I display?"))
#
# print(mountain_count,"\n","Displaying...\n")
#
# for i in range(mountain_count):
#
#     print("mountain")


#For loop with a counter

# Number_Of_Steps = int(input("How far are we from the target?"))
#
# print(Number_Of_Steps)
#
# for i in range(Number_Of_Steps, 0, -1):
#     print(i,"steps remaining")
#

# #Simple for loop
#
# brightness_level = int(input("Enter brightness level."))
#
# print("Adjusting brightness...")
#
# for i in range(0, brightness_level, 2):
#     print("Brightness level:", "*" * i)
#
# print("Complete!")


#Demoed string indexing with For

word = str(input("What word do you see?"))

print(word)

print("Displaying index positions...")

for index in range(len(word)):
    print("index:",index,"=",word[index])

print("Done!")