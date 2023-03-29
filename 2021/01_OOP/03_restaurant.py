
class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name} is serving {self.cuisine_type} food")

	def serve_custome(self, ticket_number):
		print(f"Now serving, customer: {ticket_number}")

hokben = Restaurant("hokben", "japanese")
sederharna = Restaurant("sederharna", "padang")

hokben.describe_restaurant()
sederharna.describe_restaurant()

hokben.serve_custome(98)