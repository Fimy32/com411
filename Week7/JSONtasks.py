import json

def read(path):
    with open(path, 'r') as file:
        data = json.load(file)
        return "Location", data['location'], "\nPopulation Size", data['population'], "\n" + data["bots"], "has the following stats:", data['bots']

print(read("futurama.json"))