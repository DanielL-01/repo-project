def make_pizza(size, *toppings):
	print(f"\nMaking a pizza {size}cm pizza with the following toppings:")
	for topping in toppings:
		print(f"\t--{topping}")

def make_payment(money, purchased):
	print(f"Here is your payment: {money}")
	print(f"Your change: {money-purchased}")