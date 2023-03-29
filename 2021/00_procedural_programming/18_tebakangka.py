import random

angkabenar = random.randint(0,100)
tebakan = -1


print("Tebak Angka!\n")

while tebakan != angkabenar:
	tebakan = int(input("Angkanya :"))

	if tebakan == angkabenar:
		print("Ya benar.")
	elif tebakan < angkabenar:
		print(f"Angkanya lebih besar dari {tebakan}")
	elif tebakan > angkabenar:
		print(f"Angkanya lebih kecil dari {tebakan}")