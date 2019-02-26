try:
    x=int(input("Enter a number to divide: "))
    y=int(input("Enter a number to divide by: "))
    print (x/y)
except ZeroDivisionError:
    print ("Cannot divide by zero: ")
    y=1
except ValueError:
    print("You entered an incorrect value: ")
except TypeError:
    print("The data type is invalid")