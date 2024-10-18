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
#Escape_by function

def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That just might work lets go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

listen()

identify()

escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")

