class Student:
    school = "Telusko"


    @classmethod
    def getSchool(cls):
        print("school:", cls.school)


    @staticmethod
    def info():
        print("This is Student class")


    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return ((self.m1+self.m2+self.m3)/3)

    def getm1(self):
        return self.m1

    def setm1(self, m):
        self.m1 = m


s1 = Student(30, 40, 50)
s2 = Student(35, 45, 55)

print(s1.avg())
print(s2.avg())

print (s1.info())
print(Student.info())