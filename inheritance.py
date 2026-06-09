class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def show_marks(self):
        print(f"Marks: {self.marks}")


s1 = Student("Shubham",99)
s1.show_name()
s1.show_marks()
        