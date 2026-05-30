# add = lambda a, b: a + b

# print(add(20, 10))

# mul = lambda a, b: a * b
# print(mul(10, 20))


# def evenOdd(no):
#     if no % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# print(evenOdd(10))
# print(evenOdd(11))

"""
evenOdd2 = lambda no: "Even" if no % 2 == 0 else "Odd"

print(evenOdd2(19))
print(evenOdd2(18))


pos_neg_zero = lambda n: "pos" if n > 0 else "neg" if n < 0 else "zero"

print(pos_neg_zero(10))
print(pos_neg_zero(-10))
print(pos_neg_zero(0))

"""

login = lambda user, pwd: (
    "Admin Login"
    if user == "Admin" and pwd == "007"
    else "User Login" if user == "User" and pwd == "123" else "Invalid Login"
)


print(login("Admin", "007"))
print(login("User", "123"))
print(login("Admin", "123"))
