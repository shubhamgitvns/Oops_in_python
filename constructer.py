class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


p1 = Person("Ravi", 24, "Chitaipur")
p2 = Person("Raveena", 22, "Varanasi")

p1.show()
p2.show()