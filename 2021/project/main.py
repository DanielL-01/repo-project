import os 
from settings import Settings
import json
from user import User
import time

class AnimeApp:

	def __init__(self):
		self.settings = Settings()
		self.login_attempt = 3
		self.user = 0 

	#intro, sign in, sing up 

	def intro(self):
		self.universal_clear()
		print("Welcome to CMD Anime List App")
		print("Your own personal anime list")
		input("Press ENTER to start") 

	def login(self):
		self.universal_clear()
		print("Please log in to your account first...")
		while self.login_attempt > 0:
			username = input("Username : ")
			password = input("Password : ")
			users = self.settings.users
			if username in users:
				if password == users[username]["password"]:
					print(f"Welcome back {users[username]['first']} {users[username]['last']}")
					return True
				else:
					self.universal_clear()
					print("Please try again")
					self.login_attempt -= 1
			else:
				self.universal_clear()
				print("Please try again")
				self.login_attempt -= 1

		return False	

	#Data transfer

	def load_data(self):
		try:
			with open(self.settings.user_source, 'r') as file:
				self.settings.users = json.load(file)
		except:
			self.settings.users = {}

		try:
			with open(self.settings.anime_source, 'r') as file:
				self.settings.animes = json.load(file)
		except:
			self.settings.animes = {}


	def save_data(self):
		with open(self.settings.anime_source, 'w') as file:
			json.dump(self.settings.animes, file)



	#Side op

	def universal_clear(self):
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")


	def print_genre(self, genres):
		text = ""
		for genre in genres:
			text += genre +" "
		return text

	def print_details(self, anime):
		animes = self.settings.animes
		print(f"Title : {anime.title()}")
		print(f"Genre : {self.print_genre(animes[anime]['genre']).title()}")
		print(f"Broadcast : {animes[anime]['broadcast'].title()}")
		print(f"Current episode : {animes[anime]['current episode'].title()}")
		print(f"Status : {animes[anime]['status'].title()}")
		print()


	#Main operation

	def options(self):
		selection = input("Option : ")
		animes = self.settings.animes
		if selection.lower() == "q":
			self.universal_clear()
			self.settings.activation = False

		elif selection == "1":
			self.universal_clear()
			print("ANIME LIST")
			print("---------------------------------------")
			for title, desc in animes.items():
				self.print_details(title)
			input("Press ENTER to continue")

		elif selection == "2":
			self.universal_clear()
			anime = input("Title : ").lower()
			self.universal_clear()
			if anime in animes:
				print("We found the anime you're looking for")
				self.print_details(anime)
			else:
				print(f"We couldn't find {anime} in your list.")
				print("Please try again.")
			input("Press ENTER to continue")

		elif selection == "3":
			self.universal_clear()
			count = 0
			search_genre = input("Genre : ").lower()
			self.universal_clear()
			print(f"{search_genre.title()} Animes")
			print("---------------------------------------")
			for anime in animes:
				if search_genre in animes[anime]['genre']:
					self.print_details(anime)
					count += 1
			print(f"{count} anime(s) with {search_genre } were found ")
			input("Press ENTER to continue")

		elif selection == "4":
			self.universal_clear()
			title = input("Title : ").lower()
			if title in animes:
				print(f"'{title}' is already in your list")
			else:
				genres = input("Genre (use spaces between each genres) :  ").lower()
				broadcast = input("Broadcast/Finished : ").lower()
				current_episode = input("Current Episode : ").lower()
				status = input("Status (ongoing/completed) : ").lower()
				animes[title] = {
					"genre": genres.split(),
					"broadcast":broadcast,
					"current episode":current_episode,
					"status":status
				}
				self.save_data()
				print(f"{title} was added to the list")
			input("Press ENTER to continue")

		elif selection == "5":
			self.universal_clear()
			anime = input("Title : ").lower()
			if anime in animes:
				del animes[anime]
				self.save_data()
				print(f"{anime} was removed from the list")
			else:
				print(f"We couldn't find '{anime}' from your list.")
				print("Please try again.")
			input("Press ENTER to continue")

		elif selection == "6":
			self.universal_clear()
			anime = input("Title : ").lower()
			if anime in animes:
				print("Which one do you wish to update\n1. Title\n2. Genres\n3. Broadcast\n4. Current episode\n5. Status")
				option = input("Please choose (1/2/3/4/5) : ")
				if option == "1":
					new_title = input("New title : ").lower()
					description = animes[anime]
					del animes[anime]
					animes[new_title] = description
				if option == "2":
					new_genres = input("New genre (use spaces between them) : ").lower()
					animes[anime]['genre'] = new_genres.split()
				if option == "3":
					new_broadcast_day = input("New broadcast day : ").lower()
					animes[anime]['broadcast'] = new_broadcast_day
				if option == "4":
					new_episode = input("New episode : ").lower()
					animes[anime]['current episode'] = new_episode
				if option == "5":
					new_status = input("New status : ").lower()
					animes[anime]['status'] = new_status
				print("Changes saved")
				self.save_data()
			else:
				print(f"We couldn't find '{anime}' from your list.")
				print("Please try again.")
			input("Press ENTER to continue")

	def run(self):
		self.load_data()
		self.intro()
		if self.login():
			self.settings.activation = True 
			time.sleep(2)
		while self.settings.activation:
			self.universal_clear()
			print(self.settings.menu)
			self.options()
		print("Thank you for using our app :)")



if __name__ == "__main__":
	app = AnimeApp()
	app.run()
