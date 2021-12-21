

a = 5


try:
    print("Resource Started")
    b = int(input(print("Enter dividend number:")))
    c = a/b
    print (c)

except ZeroDivisionError as e:
    print("You cannot divide a Number by zero - ", e)
except ValueError as e:
    print("Value Error - " , e)
except Exception as e:
    print("Exception - ", e)
finally:
    print("Resource Released")