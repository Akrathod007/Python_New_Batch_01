y = 20


def sayHi():
    global y
    x = 10
    y = y + 10
    print(x)
    print("Hello")
    print(y)


# print(x)

sayHi()
print(y)


x = 100


def demo():
    x = 50  # Local variable
    print(x)


demo()
print(x)
