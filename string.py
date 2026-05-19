name = "Doremon"
# city = "Japan"
city = """city"""
print(name)
print(city)

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
"""
name = "Doremon"
# name[0] = "K"  # Error
print(name)
print("Upper :", name.upper())
print("Lower :", name.lower())

m = "namaste duniya"
print("title :", m.title())

print("capitalize :", m.capitalize())

s = "heLLo WOrld"
print("swapcase :", s.swapcase())

"""

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

x = "1.1"
print(x.isdecimal())

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
"""
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

"""

# print("Hello\nWorld")
# print("Hello\tWorld")
# print("Hello\b\bWorld")
# print('"Hello"')  # "Hello"
# print("'Hello'")
# print("'''Hello'''")

# print("'hello\"")
# print("\\Hello\\")

# print("\101")
# print("\x4e")

"""
no -> 100

1 to 100:

How many prime number : 

"""
"""
no = int(input("Enter a number : "))

pc = 0

for i in range(1, no + 1):
    n = i
    f = 0
    for j in range(1, n + 1):
        if n % j == 0:
            f += 1
    if f == 2:
        print(n)
        pc += 1

print("No of Prime Numbers :", pc)

"""

# name = input("Enter a name : ")
# print(name)
# rev = ""
"""
for i in range(len(name) - 1, -1, -1):
    rev = rev + name[i]

"""
"""
for i in range(0, len(name)):
    rev = name[i] + rev
    # rev = d + "" ->d
    # rev = o + d -> od
    # rev = r + od -> rod

print("Reverse String is", rev)

"""

"""
for i in range(0, len(name)):
    print(i, "->", name[i])

for i in name:
    print(i)

"""


"""
m = Mississippi

"""


# s = input("Enter a string : ")
# vc = 0
# for i in s:
#     """
#     if (
#         i == "A"
#         or i == "a"
#         or i == "E"
#         or i == "e"
#         or i == "I"
#         or i == "i"
#         or i == "O"
#         or i == "o"
#         or i == "U"
#         or i == "u"
#     ):
#         vc += 1

#     """

#     if i in "AEIOUaeiou":
#         vc += 1
# print("Vowel Count is", vc)

"""
s = "Hello World"
u = ""

for i in s:
    u=u+i.upper()
print("Upper :",u)
"""

"""
no = 1000
1 to 1000 -> 
"""


# no = int(input("Enter a number : "))

# ld = no % 10
# fd = 0
# # ld = 1234 % 10 -> 4
# while no > 0:
#     fd = no % 10
#     no = no // 10

# print("First Digit :", fd)
# print("Lasr Digit :", ld)
# print(f"{fd} + {ld} = {fd + ld}")


# no = int(input("Enter a number : "))
# ac = 0
# for i in range(1, no + 1):
#     c = 0
#     t = i
#     t2 = i
#     sum = 0
#     while t > 0:
#         c += 1
#         t = t // 10
#     # print(f"{i} -> {c}")

#     #    12
#     while t2 > 0:
#         d = t2 % 10
#         sum = sum + d**c
#         # sum = 0 + 2 ** 2 -> 4
#         # sum = 4 + 1 ** 2 -> 5
#         t2 = t2 // 10

#     if sum == i:
#         print(i)
#         ac += 1

# print("Armstrong Number Count is", ac)

"""
1. Write a program to count total consonants in a string.

2. Write a program to remove all spaces from a string.
input : Hello World
output : HelloWorld

3. Write a program to replace all vowels with *.
input : Hello
output : H*ll*

4. Write a program to count number of words in a sentence.
input : i am python developer
output : 4

5. Write a program to print only digits from a string.
input : ansh123@gmail.com
output : 123

6. Write a program to separate uppercase and lowercase characters.
input : Hello WOrld
output : uc = HWO
         lc = ellorld

7.Write a program to find the longest word in a sentence.
input : hello python and hello javascript
output : javascript

8.Write a program to convert first character of every word into uppercase.
input : hello python and hello javascript
output : Hello Python And Hello Javascript
"""

"""
1. Write a program to count total consonants in a string.
"""

"""
s = input("Enter a string : ")
c = 0
for i in s:
    if i not in "AEIOUaeiou" and i.isalpha() == True:
        c += 1

print("Count :", c)

"""


"""
2. Write a program to remove all spaces from a string.
input : Hello World
output : HelloWorld
"""
"""
s = input("Enter a string : ")

# a = s.replace(" ", "")
a = ""

for i in s:
    if i != " ":
        a += i
print(a)

"""


"""
3. Write a program to replace all vowels with *.
input : Hello
output : H*ll*
"""
"""
s = input("Enter a string : ")
a = ""

for i in s:
    if i in "AEIOUaeiou":
        a += "*"
    else:
        a += i
print(a)

"""

"""
4. Write a program to count number of words in a sentence.
input : i am python developer
output : 4

"""
"""
s = input("Enter a string : ")
wc = 1

for i in s:
    if i == " ":
        wc += 1

print("Word Count :", wc)

"""


"""
5. Write a program to print only digits from a string.
input : ansh123@gmail.com
output : 123
"""
"""
s = input("Enter a string : ")

d = ""

for i in s:
    if i.isdigit() == True:
        d += i

print(d)

"""


"""
6. Write a program to separate uppercase and lowercase characters.
input : Hello WOrld
output : uc = HWO
         lc = ellorld
"""

"""
s = input("Enter a string : ")

uc = ""
lc = ""

for i in s:
    if i >= "A" and i <= "Z":
        uc += i
    elif i >= "a" and i <= "z":
        lc += i

print("Upper Case :", uc)
print("Lower Case :", lc)

"""


"""
7.Write a program to find the longest word in a sentence.
input : hello python and hello javascript
output : javascript
"""
"""
s = input("Enter a string : ")

words = s.split()
print(words)

longest = words[0]

for i in words:
    # len("Hello") > len("Hello") -> 5 > 5
    # len("Python") > len("Hello") -> 6 > 5
    # len(and) > len("python") -> 3 > 6
    if len(i) > len(longest):
        longest = i

print("Longest String :", longest)

"""


"""
8.Write a program to convert first character of every word into uppercase.
input : hello python and hello javascript
output : Hello Python And Hello Javascript
"""

s = input("Enter a string : ")
# print(s.title())

r = ""
new_word = True

for i in s:
    if i == " ":
        r = r + i
        new_word = True
        continue

    if new_word == True:
        r = r + i.upper()
        # r = "" + H -> H
        new_word = False
    else:
        r = r + i
        # r = H + e -> He

print("Result is :", r)
