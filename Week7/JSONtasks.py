import json

def read(path):
    with open(path, 'r') as file:
        data = json.load(file)
        return "Location", data['location'], "Population Size", data['population'], data['bots']["name"], "has the following stats:", data['bots']

print(read("futurama.json"))