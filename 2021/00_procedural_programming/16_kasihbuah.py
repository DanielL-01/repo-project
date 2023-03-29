#sebuah kantin 
#jam makan siang,
#kalau makan kurang dari/= jam 11 : salak
#kslsu makan kurang dari/= jam 13 : strawberry
#kalau kita makan kurang dari jam 12 : semangka
#kalau kita makan lewat jam 12 : sirsak
#< 11 : salak
#11 -12 : semangka
#> 12 : sirsak
time = int(input("Jam berapa : "))

#bottom to top

if time <= 11:
	print("salak")
elif time <= 12:
	print("semangka")
elif time <= 13:
	print ("strawberry")
else:
	print("sirsak")

#top to bottom

if time > 13:
	print("sirsak")
if time > 12:
	print("strawberry")
elif time > 11:
	print("semangka")	
else:
	print("salak")
