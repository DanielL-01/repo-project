
class Car:
	def __init__(self, brand, quality, owner):
		self.brand = brand
		self.quality = quality
		self.owner = owner
	def get_desciptive(self):
		print(f"This {self.quality} {self.brand} belongs to {self.owner}")


car1 = Car("mercedes", "new", "Jam")
car2 = Car("honda civic", "old", "Jom")
car3 = Car("ferrari", "broken", "Jim")
car1.get_desciptive()
car2.get_desciptive()
car3.get_desciptive()