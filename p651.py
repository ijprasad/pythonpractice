
try:
    f = open("D:/Personal/Certificates/ijp.jpg", 'rb')
    f1 = open("ijp.jpg", 'wb')


    for data in f:
        f1.write(data)
finally:
    f.close()
    f1.close()

