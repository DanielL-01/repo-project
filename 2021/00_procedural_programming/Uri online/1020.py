N = int(input())

a1 = N // 365
a2 = N % 365
b1 = a2 // 30
b2 = a2 % 30

print(f"{a1} ano(s)") 
print(f"{b1} mes(es)")
print(f"{b2} dia(s)")