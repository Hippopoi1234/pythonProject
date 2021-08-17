def greet(a, *args):
    if len(args) == 0:
        print("Hello,", a)
    else:
        print("Hello", a, end=" ")
        print(*args, sep="and", end="")
        print("!")