


a, b, c, d = map(float, input().split())


average = (a*2 + b * 3 + c * 4 + d)/10
print(f"Media: {average:.1f}")
if average  >= 7.0:
	print("Aluno aprovado.")
elif average < 5.0:
	print("Aluno reprovado.")
elif 5.0 <= average <= 6.9:
	print("Aluno em exame.")
	new = float(input())
	print(f"Nota do exame: {new:.1f}")
	new_av = (average + new)/2
	if new_av  >= 5.0:
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado." ) 
	print(f"Media final: {new_av:.1f}")
