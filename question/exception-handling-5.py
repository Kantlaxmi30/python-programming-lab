try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("a/b = %d" % c)

except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("We are in else block ")