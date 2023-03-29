import json
import random 

def saving_data(favorite_num):
	with open('data.json', 'w') as file:
		json.dump(favorite_num, file)

def loading_data():
		with open('data.json', 'r') as file:
			return json.load(file)

def guessing():
	guess_num = str(random.randint(1, 100))
	validation = input(f"Is your number {guess_num} (yes/no) ? ")
	if validation == "yes":
		return guess_num
	else:
		return input("What is your favourite number ? ")

def get_stored_number():
	try:
		loading_data()
	except:
		return 		 	

def get_fav_number():
	favorite_num = guessing()
	saving_data(favorite_num)
	return favorite_num 
	
def ask_user():
	favorite_num = get_stored_number()
	if favorite_num:
		print(f"I know your favourite number it's {favorite_num}")
	else:
		favorite_num = get_fav_number()
		print(f"I'll remember, '{favorite_num}' is your favourite number")

ask_user()