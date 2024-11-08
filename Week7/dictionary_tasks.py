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


