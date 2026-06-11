class Person:
    def __init__(self,name,age,address,phnumber):
        self.name  = name
        self.age = age
        self.address = address
        self.phnumber = phnumber

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\nPh.Number: {self.phnumber}"
    


class AccountHolder(Person):
    
    def __init__(self, name, age, address,phnumber,profession):
        super().__init__(name, age,address,phnumber)
        self.profession = profession

    def __str__(self):
        return super().__str__() + f"\nProfession: {self.profession}"
    
ah = AccountHolder("shubham",24, "Varanasi", "9022151378","Cassier")    
print(ah)