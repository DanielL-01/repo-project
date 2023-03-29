

def ask_user():
	b = float(input("novo calculo (1-sim 2-nao)"))
	if b == 1:
		return False
	elif b == 2:
		return True
	elif b < 1 or b > 2:
		return ask_user()


A_list = []

error = False

while not error:
	a = float(input())

	if 0 <= a <= 10:
		A_list.append(a)
	else:
		print("nota invalida")
	if len(A_list) == 2:
		print(f"media = {(A_list[0] + A_list[1])/2}")
		error = ask_user()
		A_list = []