#Multiple Conditions

adventure = input("What type of adventure should I have?")

if (adventure == "short") or (adventure == "dark"):
    print("Entering the dark forest!")
elif (adventure == "long") or (adventure == "safe"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")