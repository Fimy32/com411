#Dictionaries

def patterns():
 sequences = {"Short Sequence":3,"Medium Sequence":2,"Long Sequence":1}
 return sequences

def run():
    print(patterns())
    print("\n")
    display_keys(patterns())
    display_values(patterns())
    display_items(patterns())




#Iterating through a dictionary

def display_keys(data):
    for key in data:
        print(key, "\n")

def display_values(data):
    for key in data:
        print(data[key], "\n")

def display_items(data):
    for key in data:
        print(key, print(data[key]), "\n")

run()

#Nested Dictionaries

def short_pattern():
    return {"sequence":"101","occurrences":5}

def medium_pattern():
    return {"sequence":"111000","occurrences":25}

def long_pattern():
    return {"sequence":"1100110011001100","occurrences":50}

def run_task3():
    print("Analysing Patterns...")
    print({"Short_Sequence":short_pattern(),"Medium_Sequence":medium_pattern(),"Long_Sequence":long_pattern()})

run_task3()


