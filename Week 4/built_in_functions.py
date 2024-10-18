#ASCII code character checker
character = input("Program Started!\nPlease enter a standard character:")
if len(character) != 1:
    print("Error, input is not a single character.")
else:
    print("The ASCII code for",character,"is:",ord(character))
print("Program Ended!")


#ASCII code to character
valid = False
ascii_Code = int(input("Program Started!\nPlease enter an ASCII code:"))
for i in range(32,126):
    if ascii_Code == i:
        print("The character represented by the ASCII",ascii_Code,"is:",chr(ascii_Code))
        valid = True
if valid != True:
    print("The code is not valid")
print("Program Ended!")

#=