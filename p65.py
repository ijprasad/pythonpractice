

f = open('MyData', 'r')

print(f.readline(4), end="")

f1 = open("abc", 'w')
#f1.write(" Something good happening in my life")

for data in f:
    f1.write(data)


#print(f.readline())

#f.close()