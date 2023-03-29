N = int(input())

a1 = N // 3600
a2 = N % 3600
b1 = a2 // 60
b2 = a2 % 60

print(f"{a1}:{b1}:{b2}")