def greet(*args):
    print("Hello", end=" ")
    print(*args, sep="and", end="")
    print("!")
