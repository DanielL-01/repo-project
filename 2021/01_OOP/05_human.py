"""
Human -> head -> eyes, dll
         body -> Leg, Hanf, Torso, dll

"""
from random import choice

class Eyes:
	def __init__(self):
		self.color = "Black"
		self.is_big = True
		self.number = 2

class Head:
	def __init__(self):
		self.eyes = Eyes()
		
class Human:
	def __init__(self, name):
		self.name = name 
		self.age = 0
		self.sex = choice(["male", "female", "not_sure"])
		self.head = Head()
	def describe_me(self):
		print(f"Hello, I'm {self.name}, and now{self.age} years old")
jordan = Human("jordan")
print(jordan.head.eyes.color)
jesse = Human("jesse")
print(jesse.head.eyes.color)
stefani = Human("stefani")
print(stefani.head.eyes.color)

