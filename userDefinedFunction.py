# Function is block of code

"""
prime(){

    //code
}

Type of UDF:

1 no return type no arguments
2 no return type with arguments
3 return type no arguments
4 return type with arguments

"""

# 1 no return type no arguments


# def sayHi():
#     print("Hello")


# sayHi()
# sayHi()
# sayHi()
# sayHi()
# sayHi()


# 2 no return type with arguments


# def add(a, b):
#     print(f"{a} + {b} = {a + b}")


# add(10, 20)
# add(30, 20)
# add(100, 125)


# 3 with return type no arguments


# def mul():
#     no1 = int(input("Enter a number 1 : "))
#     no2 = int(input("Enter a number 2 : "))
#     # print(no1 * no2)

#     # return 0
#     return no1 * no2


# x = mul()
# print(x)

# print(mul())


# 4 with return type with arguments

"""
def isPrime(no):
    f = 0
    for i in range(1, no + 1):
        if no % i == 0:
            f += 1

    if f == 2:
        return 1
    else:
        return 0


# print(f)
no = int(input("Enter a number : "))
x = isPrime(no)

if x == 1:
    print("No is Prime")
else:
    print("No is not prime")

"""


# def toUpper():
#     name = input("Enter a name : ")

#     return name.upper()


# x = toUpper()
# print(x)


# li = [1, 2, 3, 4, 5]
# li2 = [1, 2, 3, 4, 5]
# li3 = ["Hello", "Hi", "Bye"]


# def printList(l):
#     for i in l:
#         print(i)


# printList(li)
# printList(li2)
# printList(li3)


# l1 = [1, 2, 3, 4]
# l2 = [3, 4, 5, 6]


# def commonElm(li1, li2):
#     result = []
#     for i in li1:
#         if i in li2:
#             result.append(i)

#     return result


# ans = commonElm(l1, l2)
# print(ans)

"""
def printTupel(t):
    for i in t:
        print(i)


t1 = (1, 2, 3, 4, 5)
printTupel(t1)

"""

"""
def uniqueElm(l):
    s = set(l)

    return s


x = uniqueElm([1, 2, 3, 4, 5, 1, 2, 3, 6, 5, 7, 4, 3, 2])
print(x)

"""
"""
words = ["python", "java", "ai"]


def strLength(li):
    data = {}

    for i in li:
        data[i] = len(i)

    return data


x = strLength(words)
print(x)

"""


def Math(a, b):

    return a + b, a - b, a * b, a / b, a % b, a // b, a**b


# print(Math(10, 20))
# add, sub, mul, div, mod, fdiv, power = Math(10, 20)

# print(add)
# print(sub)
# print(mul)
# print(div)
# print(mod)
# print(fdiv)
# print(power)

"""
def demo():
    return (
        10,
        1.2,
        "Hello",
        True,
        [1, 2, 3, 4],
        (1, 2, 3),
        {1, 2, 3},
        {1: 1, 2: 4, 3: 9},
    )


print(demo())

"""


# def add(a, b=10, c=20):
#     print(a + b)


# add(10)
# add(10, 50)


# def add(a, b, c):
#     print(a + b + c)


# add(c=10, a=20, b=30)

"""
def add(a, b, *args):
    print(a)
    print(b)
    print(args)


add(10, 20, 30, 40, 50, 60)


def li(*args):
    print(args)


l1 = [1, 2, 3, 4, 5]
li(l1)
li(*l1)


"""


# def demo(a, b, *args, **x):
#     print(a)
#     print(b)
#     print(args)
#     print(x)


# demo(10, 20, 30, 40, 50, name="Ram", age=21)


# def demo2(**kargs):
#     print(kargs)


# d = {"City": "Ahm", "State": "Guj"}

# demo2(**d)

"""
def sayHi():
    print("Hello")


x = sayHi

x()

"""

"""
def greet():
    print("Hello")


def call_fun(func):
    func()


call_fun(greet)

"""

"""
def outer():
    def inner():
        print("Inner Function")

    return inner


x = outer()
x()

x = outer
x()()

"""

"""
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


op = [add, sub, mul, div]
print(op)

print(op[0](10, 20))
print(op[1](10, 20))
print(op[2](10, 20))
print(op[3](10, 20))

"""


def outer():
    x = 10
    print("Outer function")

    def inner():
        nonlocal x
        print("Inner Function")
        # print(x)
        x = x + 10
        print(x)

    inner()


outer()
# inner()
# print(x)
