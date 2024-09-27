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
weight = float(input("What is your weight?"))
height = float(input("What is your height?"))
print("Your BMI is ", (weight/(height*height)*100000))
