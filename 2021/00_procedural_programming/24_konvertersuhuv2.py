import os

def cetak_pilihan():
	print("Pilihan Menu:")
	print("'cf' koversi dari celcius-fahrenheit ")
	print("'cr' koversi dari celcius-reamur ")
	print("'ck' koversi dari celcius-kelvin ")
	print("'fc' konversi dari fahrenheit-celcius ")	
	print("'fr' konversi dari fahrenheit-reamur ")
	print("'fk' konversi dari fahrenheit-kelvin ")
	print("'rf' konversi dari reamur-fahrenheit ")
	print("'rc' konversi dari reamur-celcius")
	print("'rk' konversi dari reamur-kelvin ")
	print("'kc' konversi dari kelvin-celcius")
	print("'kf' konversi dari kelvin-fahrenheit ")
	print("'kr' konversi dari kelvin-reamur ")
	print("'q' untuk keluar dari program")

#c:r:f:k = 5:4:9(+- 32):5 (+-273)

def celcius_ke_fahrentheit(suhu_c):
	return 9.0 / 5.0 * suhu_c +32
def celcius_ke_reamur(suhu_c):
	return 4/5 * suhu_c
def celcius_ke_kelvin(suhu_c):
	return 5/5 * suhu_c + 273

def fahrenheit_ke_celcius(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0
def fahrenheit_ke_reamur(suhu_f):
	return (suhu_f - 32) * 4.0 / 9.0 
def fahrenheit_ke_kelvin(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0 + 273

def reamur_ke_kelvin(suhu_r):
	return suhu_r * 5.0 / 4.0 + 273
def reamur_ke_fahrenheit(suhu_r):
	return suhu_r * 9.0 / 4.0 + 32
def reamur_ke_celcius(suhu_r):
	return 5.0 / 4.0 * suhu_r

def kelvin_ke_celcius(suhu_k):
	return 5/5 *suhu_k - 273
def kelvin_ke_fahrenheit(suhu_k):
	return (suhu_k-273)*9/5 +32
def kelvin_ke_reamur(suhu_k):
	return 4/5 * (suhu_k-273)






error = False
pilihan = None
while not error:
	os.system("cls")
	cetak_pilihan()
	pilihan = input("Pilihan:")
	if pilihan == "cf":
		main_c = float(input("Suhu Celcius-nya: "))
		result = celcius_ke_fahrentheit(main_c)
		print(f"Fahrenheit : {result}")
		input("Tekan ENTER untuk melanjut ke menu")
	elif pilihan == "cr":
		main_c = float(input("Suhu Celcius-nya: "))
		result = celcius_ke_reamur(main_c)
		print(f"Reamur : {result}")
		input("Tekan ENTER untuk melanjut ke menu")
	elif pilihan == "ck":
		main_c = float(input("Suhu Celcius-nya: "))
		result = celcius_ke_kelvin(main_c)
		print(f"Kelvin : {result}")
		input("Tekan ENTER untuk melanjut ke menu")
	elif pilihan == "fc":
		main_f = float(input("Suhu Fahrenheit-nya: "))
		print(f"Celcius : {fahrenheit_ke_celcius(main_f)}")
		input("Tekan ENTER untuk melanjut ke menu")
	elif pilihan == "fr":
		main_f = float(input("Suhu Fahrenheit-nya: "))
		result = fahrenheit_ke_reamur(main_f)
		print(f"Reamur : {result}")
		input("Tekan ENTER untuk melanjut ke menu")
	elif pilihan == "fk":
		main_f = float(input("Suhu Fahrenheit-nya: "))
		result = fahrenheit_ke_kelvin(main_f)
		print(f"Kelvin : {result}")
		input("Tekan ENTER untuk melanjut ke menu")
	elif pilihan == "kc":
		main_k = float(input("Suhu Kelvin-nya: "))
		result = kelvin_ke_celcius(main_k)
		print(f"Celcius : {result}")
		input("Tekan ENTER untuk melanjut ke menu")
	elif pilihan == "kf":
		main_k = float(input("Suhu Kelvin-nya: "))
		result = kelvin_ke_fahrenheit(main_k)
		print(f"Fahrenheit : {result}")
		input("Tekan ENTER untuk melanjut ke menu")
	elif pilihan == "kr":
		main_k = float(input("Suhu Celcius-nya: "))
		result = kelvin_ke_reamur(main_k)
		print(f"Reamur : {result}")
		input("Tekan ENTER untuk melanjut ke menu")
	elif pilihan == "rc":
		main_r = float(input("Suhu Reamur-nya: "))
		result = reamur_ke_celcius(main_r)
		print(f"Celcius : {result} ")
		input("Tekan ENTER untuk melanjut ke menu")
	elif pilihan == "rf":
		main_r = float(input("Suhu Reamur-nya: "))
		result = reamur_ke_fahrenheit(main_r)
		print(f"Fahrenheit : {result} ")
		input("Tekan ENTER untuk melanjut ke menu")
	elif pilihan == "rk":
		main_r = float(input("Suhu Reamur-nya: "))
		result = reamur_ke_kelvin(main_r)
		print(f"Kelvin : {result}")
		input("Tekan ENTER untuk melanjuti ke menu")

	elif pilihan == "q":
		error = True

	


print("Bye bye")