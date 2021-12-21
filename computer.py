

class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print("init")

    def config(self):
        print("Config is " , self.cpu, self.ram)


comp1 = Computer('i5', '16')
comp1.config()


comp2 = Computer('iddfd5', '1d6')
comp2.config()


