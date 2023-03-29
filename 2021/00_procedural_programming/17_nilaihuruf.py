"""
Guru akan memberikan nilai huruf ke siwa
dengan aturan sebagai berikut
A >= 90
B >= 80
c >= 65
d < 65

input:
Nilai angka : 85

output:
B
ketik program dibawah ini.
"""

Nilai = int(input("Nilai: "))

if Nilai >= 90:
	print("A")
elif Nilai >=80:
	print("B")
elif Nilai >=65:
	print("C")
else:
	print("D")



if Nilai < 65:
	print("D")
elif Nilai < 80:
	print("C")
elif Nilai < 90:
	print("B")
else:
	print("A")