class PyCharm:
    def execute(self):
        print("compiling")
        print("execute")

class MyEditor:
    def execute(self):
        print("spell check")
        print("Convestion Check")
        print("compiling")
        print("execute")

class Laptop:

    def code(self, ide):
        ide.execute()

ide = MyEditor()


lap1 = Laptop()
lap1.code(ide)
