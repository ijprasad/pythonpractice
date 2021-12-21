
def person(name, **var):
    print(name)
    for i, j in var.items():
        print(i)
        print(j)
    print(var)



person('Inderjeet', age=40, city='hyderabad', phone=9384394823)