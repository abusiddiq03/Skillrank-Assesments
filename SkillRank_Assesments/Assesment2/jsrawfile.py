import json
with open('Assesment2\ex5.json', 'r') as json_file:
    ex5 = json.load(json_file)
 
for donut in ex5:
    if donut.get('name') == "Old Fashioned" and donut.get('type') == "donut":
        
        donut['batters']['batter'].append({"id": "1005", "type": "Tea"})
        break  

with open('Assesment2\ex5.json', 'w') as json_file:
    json.dump(ex5, json_file, indent=4)

print("Updated JSON data successfully.")
print(json.dumps(ex5, indent=4))