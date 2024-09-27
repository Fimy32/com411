# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")
#An f-string can be used to format output allowing us to combine our message with the value of our variable


# Display a robot with user's eyes
print("Please enter a character for the eye")
eye = input()
print("The robots expression is as follows:")
print("\\        /")
print("##########")
print(f"# {eye}    {eye} #")
print("#  ____  #")
print("##########")

#BMI Calculator
name = str(input("What is your name?"))
age = int(input("What is your age?"))
weight = float(input("What is your weight(KG)?"))
height = float(input("What is your height(M)?"))
print("Hello",name,"your age is", age,"and your BMI is", (weight/(height ** 2)))

#Operator Demonstration
lives = int(input("Please enter the number of lives."))
energy = int(input("Please enter the energy level."))
shield = int(input("Please enter the shield level."))
print("Lives:", "♥" * lives)
print("Energy:", "♦" * energy)
print("Shield:", "♦" * shield)
