import os
from settings import Settings
import json
from getpass import getpass
from user import User
from contacts import Contact
class ContactApp:

	def __init__(self):
		self.settings = Settings()
		self.login_attempt = 0
		self.user = None

	def clear_screen(self):
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")

	def show_menus(self):
		self.clear_screen()
		print("Welcome...",self.user.first.title(),self.user.last.title())
		print(self.settings.menu)
		
	def load_data(self):
		try:
			with open(self.settings.users_location, 'r') as file:
				self.settings.users = json.load(file)
		except:
			self.settings.users = {}

		try:
			with open(self.settings.contacts_location, 'r') as file:
				self.settings.contacts = json.load(file)
		except:
			self.settings.contacts = {}
		#rint(self.settings.users)
		#print(self.settings.contacts)

	def save_data(self):
		with open(self.settings.contacts_location, 'w') as file:
			json.dump(self.settings.contacts, file)

	def logger(self):
		self.user = User(username="admin", first="Admin", last="Admin", password="12345")
		return True
		self.clear_screen()
		while self.login_attempt < 3:
			print("\nPlease login")
			username = input("Username\t: ")
			password = getpass("Password\t: ")

			if username in self.settings.users:
			 	if self.settings.users[username]["password"] == password:
			 		self.user = User(
			 			username,
			 		 	first=self.settings.users[username]["first"],
			 			last=self.settings.users[username]["last"],
			 			password=self.settings.users[username]["password"] 
			 			)
			 		return True

			else:
				self.login_attempt += 1
				print("Login Failed")
		return False

	def find_contact(self, phone):
		contacts = self.settings.contacts
		if phone in contacts:
			print("contact found")
			print(f"Full name: {contacts[phone]['first'].title()} {contacts[phone]['last'].title()}")
			print(f"Phone: {phone}")
			print(f"Address: {contacts[phone]['address']}")
			return True

		print("contact doesn't exists")
		return False

	def check_option_user(self, char):
		if char == "q":
			self.settings.active = False
		elif char == "1":
			self.clear_screen()
			#print(self.settings.contacts)
			contacts = self.settings.contacts
			print("Nomor\t\tNama Lengkap\t\tAlamat")

			for phone, contact in contacts.items():
				print(f"{phone}\t{contact['first'].title()} {contact['last'].title()}\t\t{contact['address']}")
			
			input("Press Enter to Return") 
		elif char == "2":
			self.clear_screen()
			phone = input("Enter phone number: ")

			self.find_contact(phone)

			input("Press Enter to Return")
		elif char == "3":
			self.clear_screen()
			first = input("First : ")
			last = input("Last : " )
			phone = input("Phone : ")
			address = input("Address : ")
			contact = Contact(first, last, phone, address)
			self.settings.contacts[contact.phone] = {
				"first" : contact.first,
				"last" : contact.last,
				"address" : contac.taddress
			}
			self.save_data()
			print("Contacts saved!")
			input("Press Enter to Return")
		elif char == "4":
			self.clear_screen()
			phone = input("Phone : ")
			if self.find_contact(phone):
				print("Edit\n1. Phone, 2. First, 3. Last, 4. Address")
				option = input("Which data do you want to update ? (1/2/3/4) ")
				if option == "1":
					new_phone = input("New phone number : ")
					old_contact = self.settings.contacts[phone]
					self.settings.contacts[new_phone] = {
						"first" : old_contact["first"],
						"last" : old_contact["last"],
						"address": old_contact["address"]
					} 
					del self.settings.contacts[phone]
					self.save_data()
					print("New phone number saved")
				elif option == "2":

					first = input("New first name : ")
					self.settings.contacts[phone]["first"] = first
					self.save_data()
					print("New first name saved")

				elif option == "3":
					last = input("New last name : ")
					self.settings.contacts[phone]["last"] = last
					self.save_data()
					print("New last name saved")

				elif option == "4":
					address = input("New address : ")
					self.settings.contacts[phone]["address"] = address
					self.save_data()
					print("New address saved")

			input("Press Enter to Return.")

		elif char == "5":
			self.clear_screen()
			phone = input("Phone : ")
			if self.find_contact(phone):
				confirm = input("Are you sure to delete thsi contact ? (y/n) ")
				if confirm.lower() == "y":
					del self.settings.contacts[phone]
					self.save_data()
					print("contact deleted")
			input("Press Enter to Return")

	def run(self):
		self.load_data()
		if self.logger():
			self.settings.active = True
		while self.settings.active:
			self.show_menus()
			self.check_option_user(input("Option: ").lower())



if __name__ == "__main__":
	app = ContactApp()
	app.run()