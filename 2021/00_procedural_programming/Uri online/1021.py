N = float(input())

notes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01] 

b = N * 100 
print("NOTAS:")
for j in notes:
	a = b // (j * 100)
	print(f"{int(a)} nota(s) de R$ {j:.2f}")
	b = b % (j * 100)
print("MOEDAS:")
for i in coins:
	a = b // (i * 100)
	print(f"{int(a)} moeda(s) de R$ {i:.2f}")
	b = b % (i * 100)
	