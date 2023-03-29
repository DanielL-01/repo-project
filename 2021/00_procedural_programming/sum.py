a = 1
s = 0


print("Enter Numbers to add to the sum.")
print("Enter q to quit.")
while a != "q":                           
    print("Current Sum:", s)            
    a = input("Number?" )
    if a == "q":
        print("Total sum:", s)
    else:
        s = s + float(a)
        a = str(a)


        



                                