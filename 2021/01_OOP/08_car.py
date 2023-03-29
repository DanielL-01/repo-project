#inheritance

class Car:
	def __init__ (self, make, model, year, colour, new, manual):
		self.make = make
		self.model = model
		self.year = year
		self.colour = colour
		self.new = new 
		self.manual = manual
		self.odometer = 0

	def get_desciptive(self):
		return f"This car is a {self.make}'s  car\nIts model is {self.model}-{self.year}.\nIt has {self.colour} colour."

	def increment_odometer(self, kms):
		self.odometer += kms
		print(f"The odometer has been updated to {self.odometer}kms.")

	def fill_gas_tank(self):
		print(f"The car is full of fuel right now!.")

	def change_colour(self, new_colour):
		self.colour = new_colour
		print(f"The colour is changed into {self.colour}")

class ElectricCar(Car):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.battery = {"capacity":100, "size":5000}
	# def __init__(self, make, model, year, colour, new, manual):
	# 	super().__init__(make, model, year, colour, new, manual)
		#Car.__init__(self, make, model, year, colour, new, manual)
	def fill_gas_tank(self):
		print("This car doesn't need a gas ...")

	def charge_battery(self):
		print("This car is fully charged")


class ElectricBus(ElectricCar):
	def __init__(self, make, model, year, colour, new, manual):
		super().__init__(make, model, year, colour, new, manual)
		self.battery = {"capacity":100, "size":10000}
		self.seats =  26
	def get_desciptive(self):
		return f"This bus is a {self.make}'s  bus\nIts model is {self.model}-{self.year}.\nIt has {self.colour} colour."

	def arriving_busstops(self):
		print(f"This bus is stopping at the next bus stop with {self.seats} free seats")
	#1 special attribute self.anything
	#1 special method def anything(self, )
hyundai = ElectricCar("Hyundai", "kona ev", 2020, "black", True, False)
print(hyundai.get_desciptive())
hyundai.fill_gas_tank()
hyundai.charge_battery()

danlee = ElectricBus("Danlee", "Xt bus", 2021, "silver", True, False)
print(danlee.get_desciptive())
danlee.arriving_busstops()

# toyota = Car("toyota", "yaris", 2020, "black", True, True)
# print(toyota.get_desciptive())
# toyota.increment_odometer(100)
# toyota.fill_gas_tank()
# toyota.change_colour("blue")