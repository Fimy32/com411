#ASCII code character checker
character = input("Program Started!\nPlease enter a standard character:")
if len(character) != 1:
    print("Error, input is not a single character.")
else:
    print("The ASCII code for",character,"is:",ord(character))
print("Program Ended!")


#ASCII code to character
ascii_Code = int(input("Program Started!\nPlease enter an ASCII code:"))
if range(ascii_Code) == (32,126):
    print("The character represented by the ASCII",ascii_Code,"is:",chr(ascii_Code))
else:
    print("The code is not valid")
print("Program Ended!")

