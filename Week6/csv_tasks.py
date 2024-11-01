import csv

def read_csv(path):
    with open(path, "r") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for value in csv_reader:
            print(value)


read_csv("clothing.csv")