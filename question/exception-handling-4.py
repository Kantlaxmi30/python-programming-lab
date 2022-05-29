try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("The answer of a divide by b:", c)

except ZeroDivisionError:
    print("Can't divide with zero")
finally:
    print("Inside a finally block")