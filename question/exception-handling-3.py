##specifiy two exceptions in the single except clause.

try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("The answer of a divide by b:", c)
except(ValueError, ZeroDivisionError):
    print("Please enter a valid value")