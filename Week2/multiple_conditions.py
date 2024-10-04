#Multiple Conditions

adventure = input("What type of adventure should I have?")

if (adventure == "short") or (adventure == "dark"):
    print("Entering the dark forest!")
elif (adventure == "long") or (adventure == "safe"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")

#AND operator

hear = input("What did I hear?")
see = input("What did I see?")
print(hear,see)
if (hear == "grrr") and (hear == "two red eyes"):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")