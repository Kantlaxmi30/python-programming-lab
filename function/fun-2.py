##Create a function with variable length of arguments

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)