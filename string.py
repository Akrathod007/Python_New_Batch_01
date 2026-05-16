# name = "Doremon"
# # city = "Japan"
# city = """city"""
# print(name)
# print(city)

msg = """
qwe
qrw
fwef
ewfwef
ewfw
"""
"""
print(msg)

m = "Shinchan"
#    01234567
# -ve87654321
print(m)
print(m[0])
print(m[3])
print(m[-1])
print(m[-4])

print(m[1:6])  # 1 to 5
print(m[1:])
print(m[:7])
print(m[1:7:3])
print(m[:])
print(m[::2])
print(m[-2:-7])
print(m[-7:-2])
print(m[::-1])
# print(m[1:7:-1])
print(m[-2:-7:-1])
print(m[-2:-8:-2])
print(m[2:-2])
print(m[3:-2])
print(m[-2:3])


"""
# Case Conversion :

# name = "Doremon"
# name[0] = "K" #Error
# print(name)
# print("Upper :", name.upper())
# print("Lower :", name.lower())

# m = "namaste duniya"
# print("title :", m.title())

# print("capitalize :", m.capitalize())

# s = "heLLo WOrld"
# print("swapcase :", s.swapcase())


# Searching & Finding :
"""
msg = "Mississippi"
print(msg)
print(msg.find("i"))
print(msg.find("i", 4))
print(msg.find("i", 5, 9))
print(msg.find("q"))
print(msg.find("ss"))

print(msg.rfind("i"))
print(msg.rfind("i", 1, 7))

print(msg.rfind("i", -7, -2))
print(msg.index("i"))
# print(msg.index("q"))  #Error
print(msg.rindex("i"))
# print(msg.rindex("pq")) #Error

print(msg.startswith("Mi"))
print(msg.startswith("Mi", 3))
print(msg.startswith("s", 3))
print(msg.startswith("ss", 2, 8))
print(msg.startswith("ss", 3, 8))

print(msg.endswith("pi"))
print(msg.endswith("pi", 2))
print(msg.endswith("pi", 2, 8))

"""
# Modification & Replacement :
"""
m = "      Hello World    "
print(m.strip())
print(m.lstrip())
print(m.rstrip())

print(m.replace("o", "a"))
print(m.replace("ll", "m"))

"""

# Splitting & Joining :
"""
a = "a b c d e"
print(a.split())

email = "demo@gmail.com"
print(email.split("@"))

x = "a-b-c-d-e"
print(x.split("-", 2))
print(x.rsplit("-"))
print(x.rsplit("-", 2))

y = "Hello\nHi\nBye"
print(y.splitlines())


print("$".join(["a", "b", "c", "d"]))

"""

# Checking Content :
"""
x = "123abc"
print(x.isalnum())

x = "123"
print(x.isalnum())

x = "abc"
print(x.isalnum())

x = "###dfwef"
print(x.isalnum())

"""
"""
x = "abc"
print(x.isalpha())

x = "123abc"
print(x.isalpha())

x = "123"
print(x.isdigit())

x = "123abc"
print(x.isdigit())

x = "123"
print(x.isdecimal())

x = "⁰"
print(x.isdigit())
print(x.isdecimal())

x = "⅔"
print(x.isnumeric())

x = "123"
print(x.isnumeric())

x = "123.2"
print(x.isnumeric())

"""

"""
x = "var1"
print(x.isidentifier())

x = "1var"
print(x.isidentifier())

x = "var_1"
print(x.isidentifier())

x = "_"
print(x.isidentifier())


x = "                 "
print(x.isspace())

x = "        1323        "
print(x.isspace())

x = "hello"
print(x.islower())

x = "Hello"
print(x.islower())

x = "HELLO"
print(x.isupper())

x = "Hello"
print(x.isupper())

x = "Hello World"
print(x.istitle())

x = "Hello WOrld"
print(x.istitle())

"""

# Alignment & Formatting :

x = "Hi"

print(x.center(10, "-"))
print(x.center(10))

print(x.ljust(10, "-"))
print(x.rjust(10, "-"))

x = "Bye"
print(x.center(10, "-"))
print(x.ljust(10, "-"))
print(x.rjust(10, "-"))

x = "42"
print(x.zfill(10))

name = "Doremon"
age = 21

print("Name is {} and age is {}".format(name, age))
print("Name is {} and age is {}".format(age, name))

print("Name is {name}".format_map({"name": "Ansh"}))

print(len(name))
print("Name is", name, "age is", age)
print(f"Name is {name} and age is {age}")

print("My name is %s and I am %d years old." % (name, age))
# print("My name is %s and I am %d years old." % (age, name))


print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\b\bWorld")
print('"Hello"')  # "Hello"
print("'Hello'")
print("'''Hello'''")

print("'hello\"")
print("\\Hello\\")

print("\101")
print("\x4e")
