class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop("HP", 'i5', 16)

    def show(self):
        print (self.name, self.rollno)

    class Laptop:
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Inderjeet', 4)
s2 = Student('Krishna', 6)

s1.show()
s1.lap.show()


