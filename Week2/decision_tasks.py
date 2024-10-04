#IF statement Demo

book_Type = input("What type of book do you like?")
if book_Type == "adventure":
    print("I like",book_Type,"books!")
print("Finished reading book")


#IF ELSE statement Demo

activity_Type = input("Please enter an activity.")
if activity_Type == "calculate":
    print("Performing calculations...")
else:
    print("Performing",activity_Type + "...")
print("Finished reading book")

#Robot moving Demo

direction = input("Towards which direction should I go (up, down, left or right)?")
if (direction == "up"):
    print("I am moving in an upward direction!")
elif (direction == "down"):
    print("I am moving in a downward direction!")
else:
    print("I am moving",direction + "!")

#Modulous Operator

number = int(input("Please enter a whole number:"))
if (number % 2 != 0):
    print("Odd")
else:
    print("Even")