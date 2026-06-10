class Person:
    def __init__(self, name,age,address):
        self.name = name
        self.age = age
        self.address = address


    def show_genral_info(self):
        print(f"Name: {self.name},", f"Age: {self.age},", f"Address: {self.address}")


class Employee(Person):
    def __init__(self, name, age, address,post):
        super().__init__(name, age,address)
        self.post = post

    def show_imploye_info(self):
         print(f"Post: {self.post}")

class Manager(Employee):
    def __init__(self, name, age, address, post, department):
        super().__init__(name, age, address, post)
        self.department = department

    def show_manager_info(self):
        print(f"Department: {self.department}")         

m = Manager("shubham", 24, "Varanasi", "Data Scientest","AI-ML")
m.show_genral_info()
m.show_imploye_info()
m.show_manager_info()

# class Student(Person):
#     def __init__(self, name, marks):
#         super().__init__(name)
#         self.marks = marks

#     def show_marks(self):
#         print(f"Marks: {self.marks}")


# s1 = Student("Shubham",99)
# s1.show_name()
# s1.show_marks()
        