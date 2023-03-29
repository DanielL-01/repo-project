class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_name(self):
        print(f"My name is {self.name}")

    def isAdultInst(self):
        return self.age >= 18
    
    @staticmethod #create untuk dijalankan tnapa membuat instance object
    def isAdult(age):
        return age>=18
    



anas = Person("Anas", 10)

print(Person.isAdult(20))
print(anas.isAdultInst())
print(anas.isAdult(10))
anas.display_name()