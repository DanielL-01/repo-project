import json
import random


def load_data():
	try:
		with open('data.json', 'r') as file:
			return json.load(file)
	except:
		return {}

def save_data(data_master):
	with open('data.json', 'w') as file:
		json.dump(data_master, file)
		return True

def greet_user(data_master):
	username = input("What is your name ? ")
	if username in data_master:
		print(f"Welcome back {username}")
	else:
		data_master[username] = None
		save_data(data_master)
		print("We'll remember you when you come back")
	return username

def get_fav_number(guess):
	guess = random.randint(0, 100)
	ans = input(f"I'll guess your favourite number is {guess}, is it right (y/n)")
	if ans.lower() == "y":
		return  guess
	elif ans.lower() == "n":
		try:
			num = int(input("So, what is your favourite ? "))
		except:
			print("Please input an integer")
			return get_fav_number(guess)
		return num
	else:
		print("Please, answer with y or n!")
		return get_fav_number(guess)


def change_number(data_master, username):
	yn = input("Do you want to change your number (y/n)")
	if yn == "y":
		new_fav_number = int(input("What is your new favourite number? "))
		data_master[username] = new_fav_number
		save_data(data_master)
		print("We'll remember your new favourite number next time")
	elif yn == "n":
		print("ok")
	else:
		print("Please input y or n")

def ask_user(data_master, username):
	#print(data_master, username)
	if username in data_master:
		if data_master[username]:
			print(f"I know your favourite number, it is {data_master[username]}")
			change_number(data_master, username)
		else:
			guess = random.randint(0, 100)
			favorite_num = get_fav_number(guess)
			data_master[username] = favorite_num
			save_data(data_master) 
			print("We'll remember your favourite number next time")


data_master = load_data()

ask_user(data_master, greet_user(data_master))