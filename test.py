import json

file = open('response.json')

r = json.load(file)

for i in r:
    print(i['domain'])