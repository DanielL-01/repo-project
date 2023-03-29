x, y = input().split()
x, y = int(x), int(y)

if x == 1:
	total = 4 * y
	print(f"Total: R$ {total:.2f}")
elif x == 2:
	total = 4.5 * y
	print(f"Total: R$ {total:.2f}")
elif x == 3:
	total = 5 * y
	print(f"Total: R$ {total:.2f}")
elif x == 4:
	total = 2 * y
	print(f"Total: R$ {total:.2f}")
elif x == 5:
	total = 1.5 * y
	print(f"Total: R$ {total:.2f}")