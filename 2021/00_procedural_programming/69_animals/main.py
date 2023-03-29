import json

with open('data.json', 'r') as file:
	owners = json.load(file)

#print(owners) 
for owners, pets in owners.items():
	print(f"-{owners}")
	for pet in pets:
		print(f"\t{pet}")