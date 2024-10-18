import random

def Guess_Number():
    minimum = int(input("Enter Minimum"))
    maximum = int(input("Enter Maximum"))
    number = random.randint(minimum, maximum)
    tries = int(0)
    guess = int(24356786243786543567864356345676456754675464357423564354653546354663555555555555)
    print("I am thinking of a number between",minimum,"and",maximum,". Can you guess what it is?")
    while guess != number:
        guess = int(input("Guess a number: "))
        if guess < number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        print("Try Again!")
        tries += 1
    print("Congratulations! You guessed my number in",tries,"tries!")

Guess_Number()