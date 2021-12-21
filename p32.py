

def greet():
    print("Hello")
    print("Good Morning")

def add(x, y):
    return x + y


def add(a, b):
    c = a + b
    print(c)
    return 1

def add_sub(a, b):
    c = a + b
    d = a - b
    return c, d


greet()
result1, result2 = add_sub(4, 5)
print(result1, result2)
