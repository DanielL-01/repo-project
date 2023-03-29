# N = float(input())

# print(int(N))
# a1 = N // 100.00
# print(f"{int(a1)} nota(s) de R$ 100,00")
# a2 = N % 100.00

# b1 = a2 // 50.00
# print(f"{int(b1)} nota(s) de R$ 50,00")
# b2 = a2 % 50.00


# c1 = b2 // 20.00
# print(f"{int(c1)} nota(s) de R$ 20,00")
# c2 = b2 % 20.00

# d1 = c2 // 10.00
# print(f"{int(d1)} nota(s) de R$ 10,00")
# d2 = c2 % 10.00

# e1 = d2 // 5.00
# print(f"{int(e1)} nota(s) de R$ 5,00")
# e2 = d2 % 5.00

# f1 = e2 // 2.00
# print(f"{int(f1)} nota(s) de R$ 2,00")
# f2 = e2 % 2.00

# g1 = f2 / 1.00
# print(f"{int(g1)} nota(s) de R$ 1,00")


money = int(input())
banknotes = [100, 50, 20, 10, 5, 2, 1]

counter = 0 
while counter < len(banknotes):
	note = money // banknotes[counter]
	money = money%banknotes[counter]
	print(f"{note} nota(s) de R$ {banknotes[counter]},00")
	counter += 1