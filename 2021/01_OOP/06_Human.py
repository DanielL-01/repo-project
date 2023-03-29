
from random import choice

class Eyes:
	def __init__(self):
		self.color = "Black"
		self.is_big = True
		self.number = 2

class Mouth:
	def __init__(self, Humaninfo):
		self.human = Humaninfo

	def describe_about_sex(self):
		print(f"I am {self.human.sex}")
class Head:
	def __init__(self, Humaninfo):
		self.human = Humaninfo
		self.eyes = Eyes()#obj in obj atau obj as an attribute
		self.mouth = Mouth(self.human) #mouth(HumanInfo)
class Human:
	def __init__(self, name):
		self.name = name 
		self.age = 0
		self.sex = choice(["male", "female", "not_sure"])
		self.head = Head(self)

	def describe_me(self):
		print(f"Hello, I'm {self.name}, and now{self.age} years old")

	def describe_eyes(self):
		return f"I have {self.head.eyes.number} eyes"
jordan = Human("jordan")
print(jordan.head.eyes.color)
print(jordan.describe_eyes())
jordan.head.mouth.describe_about_sex()

