
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

greater = (a+b+abs(a-b))/2
greater2 = (greater + c + abs(greater - c) )/ 2
print(int(greater2),"eh o maior")

