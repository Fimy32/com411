#Text based Adventure game

#Listen Function

def listen():
    sound = input("Enter a sound")
    print("That was a loud",sound + "!")

#Identify Function

def identify():
    obstacle = input("What do you see?")
    if obstacle != "a large boulder":
        print("We should be fine.")
    else:
        print("We should run!")

listen()

identify()

