def sayHi():
    print("Hello")


def PrimeCheck(no):
    f = 0

    for i in range(1, no + 1):
        if no % i == 0:
            f += 1

    if f == 2:
        print("Prime")
    else:
        print("Not Prime")


def printList(li):
    for i in li:
        print(i)
