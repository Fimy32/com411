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

def cross_bridge(steps_crossed):
    for i in range(steps_crossed):
        print("Crossed step")
    if steps_crossed >= 5:
        print("The bride is collapsing!")
    else:
        print("We must keep going!")

#Climb Ladder Function

def climb_ladder(steps_remaining, steps_completed):
    if steps_remaining > steps_completed:
        print("Still some way to go!")
    else:
        print("We are almost there!")

def display_ladder(steps):
    print("|---|\n" * steps)

def create_ladder():
    display_ladder(int(input("How many steps remain?")))

listen()

identify()

escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")

cross_bridge(3)
cross_bridge(6)

climb_ladder(5,2)
climb_ladder(2,5)

create_ladder()


