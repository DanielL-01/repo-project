
with open('data.txt', 'r') as file:
	fruits = file.read()

print(fruits)
fruit = fruits.split("\n")
print(fruit)