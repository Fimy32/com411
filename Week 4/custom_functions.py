#Text based Adventure game

#Listen Function

# def listen():
#     sound = input("Enter a sound")
#     print("That was a loud",sound + "!")
#
# #Identify Function
#
# def identify():
#     obstacle = input("What do you see?")
#     if obstacle != "a large boulder":
#         print("We should be fine.")
#     else:
#         print("We should run!")
# #Escape_by function
#
# def escape_by(plan):
#     if plan == "jumping over":
#         print("We cannot escape that way! The boulder is moving too fast!")
#     elif plan == "cross bridge ahead":
#         print("That just might work lets go!")
#     else:
#         print("We cannot escape that way! The boulder is in the way!")
#
# def cross_bridge(steps_crossed):
#     for i in range(steps_crossed):
#         print("Crossed step")
#     if steps_crossed >= 5:
#         print("The bride is collapsing!")
#     else:
#         print("We must keep going!")
#
# #Climb Ladder Function
#
# def climb_ladder(steps_remaining, steps_completed):
#     if steps_remaining > steps_completed:
#         print("Still some way to go!")
#     else:
#         print("We are almost there!")
#
# def display_ladder(steps):
#     print("|---|\n" * steps)
#
# def create_ladder():
#     display_ladder(int(input("How many steps remain?")))
#
# def sum_weights(char_weight, inven_weight):
#     return char_weight + inven_weight
#
# def calc_avg_weight(char_weight, inv_weight):
#     return sum_weights(char_weight, inv_weight) / 2
#
# def run():
#     weight = int(input("Enter character weight"))
#     inventory_weight = int(input("Enter inventory weight"))
#     if input("Sum or Weight?") == "Sum":
#         print(sum_weights(weight, inventory_weight))
#     else:
#         print(calc_avg_weight(weight, inventory_weight))
#
#
# listen()
#
# identify()
#
# escape_by("jumping over")
# escape_by("running around")
# escape_by("cross bridge ahead")
#
# cross_bridge(3)
# cross_bridge(6)
#
# climb_ladder(5,2)
# climb_ladder(2,5)
#
# create_ladder()
#
# run()

def display_in_box(word):
    return "-------------\n|\n|\n|\n|\n|\n|" + word + "|\n|\n|\n|\n|\n-------------"

def display_lower_case(word):
    return word.lower()

def display_upper_case(word):
    return word.upper()

def display_mirrored(word):
    return word.reverse()

def repeat(word):
    count = input("How many times?")
    upper = True
    for i in range(int(count)):
        upper = not upper
        if upper:
            print(word.upper())
        else:
            print(word.lower())

def map():
    word = input ("Enter a word")
    option = input("What do you want to do to the word? (1-5)")
    if option == "1":
        print(display_in_box(word))
    elif option == "2":
        print(display_lower_case(word))
    elif option == "3":
        print(display_upper_case(word))
    elif option == "4":
        print(display_mirrored(word))
    elif option == "5":
        repeat(word)


map()


