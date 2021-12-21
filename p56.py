class A:

    def __init__(self):
        print("In A Init")

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B():
    def __init__(self):

        print("In B Init")

    def feature1(self):
        print("Feature B1 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("In C Init")

    def feature4(self):
        print("Feature C4 is working")



a1 = C()

a1.feature1()
a1.feature2()
