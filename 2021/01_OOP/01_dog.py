
class Dog:
	def __init__(self, name): #fungsi contructor
		self.name = name 
		self.age = 0
		self.isCute = True


	def roll_over(self):
		print(f"{self.name} rolled over...")
	def sleep(self):
		print(f"{self.name}: zzzz")
	def bark(self):
		print(f"{self.name}: argghhh")


moly = Dog("moly")
print(moly.name)
print(moly.age)
print(moly.isCute)
moly.roll_over()

holy = Dog("holy")
print(holy.name)
holy.roll_over()


doly = Dog("doly")
print(doly.name)
print(doly.age)
print(doly.isCute)
doly.roll_over()
doly.sleep()
doly.bark()