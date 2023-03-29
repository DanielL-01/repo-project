#Changing Adding and Removing Elements

motors = ["honda legenda", "yamaha fizr", "suzuki shogun"]
print(motors)
#changing / modifying
motors[1] = "ducati"
print(motors)
#adding elements
motors.append("kawasaki")
print(motors)


#inserting element
motors.insert(0, "tvs")
print(motors)

motors.insert(2, "viar")
print(motors)

#removing
motors.pop(2) # menggunakan index
print(motors)


motors.remove("tvs") # menggunakan data
print(motors)

del motors[0]
print(motors)