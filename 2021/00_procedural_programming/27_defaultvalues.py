def describe_pet(pet_name= "John", animal_type= "dog"):
	"""Dsiplay information about a pet"""
	print(f"I have a {animal_type}")
	print(f"My {animal_type}'s name is {pet_name.title()}")
	# .lower() , .upper()
describe_pet('harry doughnat', 'hamster' )
describe_pet("willie")


#equivalent function
describe_pet("willie", "dog")
describe_pet(animal_type="dog", pet_name="willie")
describe_pet("willie")
describe_pet(pet_name="willie", animal_type="dog")

describe_pet("ollie", "fish")

describe_pet()