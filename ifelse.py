# no1 = int(input("Enter a number 1 : "))
# no2 = int(input("Enter a number 2 : "))

# print(no1 + no2)

"""
no = int(input("Enter a number : "))

if no > 0:
    print("Number is Positive")
elif no < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

"""

# no = int(input("Enter a number : "))

# if no % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

"""
7 -> 00000111
1 -> 00000001
---------------
& -> 00000001 -> 1
"""

"""
if no & 1 == 0:
    print("Even")
else:
    print("Odd")

"""

"""
10 // 2 -> 5 * 2 = 10 == 10

11 // 2 -> 5 * 2 = 10 == 11

"""

"""
if no // 2 * 2 == no:
    print("Even")
else:
    print("Odd")

"""


"""
m1 = float(input("Enter a marks 1 :"))
m2 = float(input("Enter a marks 2 :"))
m3 = float(input("Enter a marks 3 :"))
m4 = float(input("Enter a marks 4 :"))
m5 = float(input("Enter a marks 5 :"))


total = m1 + m2 + m3 + m4 + m5

per = total / 5

print("Total :", total)
print("Percentage :", per)

if per >= 90:
    print("Grade A")
elif per >= 80:
    print("Grade B")
elif per >= 70:
    print("Grade C")
elif per >= 60:
    print("Grade D")
elif per >= 50:
    print("Grade E")
else:
    print("Grade F")

"""

"""
if con:

if con:

if con:

"""


"""
no1 = int(input("Enter a number 1 : "))
no2 = int(input("Enter a number 2 : "))

if no1 > no2:
    print("No1 is bigger")
elif no1 < no2:
    print("No2 is bigger")
else:
    print("Both Numbers are Equal")

"""
"""
num = int(input("Enter a number : "))

if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
elif num < 0:
    if num % 2 == 0:
        print("Negative Even Number")
    else:
        print("Negative Odd Number")
else:
    print("Number is Zero")

"""

# Amt = 1260

"""
n500 - 2 -> 1260 - 1000 -> 260
n100 - 2 -> 260 - 200 -> 60
n50 - 1 -> 60 - 50 -> 10
n20 - 0
n10 - 1 -> 10 - 10 -> 0
n5 - 0
n2 - 0
n1 - 0
"""

# Amt = int(input("Enter a Amount : "))  # 1260

# n500 = n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0

# if Amt >= 500:
#     n500 = Amt // 500  # n500 ->
#     Amt = Amt - n500 * 500
#     # Amt = 1260 - 2 * 500 => 1260 - 1000 -> 260

#     """
#          2
#         -------
#      500|1260
#          1000
#          -----
#           260


#     """
# if Amt >= 100:
#     n100 = Amt // 100
#     Amt = Amt - n100 * 100

# if Amt >= 50:
#     n50 = Amt // 50
#     Amt = Amt - n50 * 50

# if Amt >= 20:
#     n20 = Amt // 20
#     Amt = Amt - n20 * 20

# if Amt >= 10:
#     n10 = Amt // 10
#     Amt = Amt - n10 * 10

# if Amt >= 5:
#     n5 = Amt // 5
#     Amt = Amt - n5 * 5

# if Amt >= 2:
#     n2 = Amt // 2
#     Amt = Amt - n2 * 2

# if Amt >= 1:
#     n1 = Amt // 1
#     Amt = Amt - n1 * 1


# print("N500 :", n500)
# print("N100 :", n100)
# print("N50 :", n50)
# print("N20:", n20)
# print("N10 :", n10)
# print("N5 :", n5)
# print("N2 :", n2)
# print("N1 :", n1)


# a = 40
# b = 20

# result = "a is bigger" if a > b else "b is bigger"
# print(result)


"""
1st condition output (if 1st con) else 2nd condition output (if 2nd con) else 3rd condition output (if 3rd con) else output
"""
"""
per = int(input("Enter a Percentage : "))

result = (
    "Grade A"
    if per >= 90
    else (
        "Grade B"
        if per >= 80
        else (
            "Grade C"
            if per >= 70
            else "Grade D" if per >= 60 else "Grade E" if per >= 50 else "Grade F"
        )
    )
)

print(result)   

"""


"""
pass in Python : The pass statement is a null operation — it does nothing when executed.
It is mainly used as a placeholder where code will be written later, or where Python expects a statement but 
you don’t want to write anything yet.
"""

# if 5 > 2:
#     pass


# a = chr(65)
# print(a)


# b = ord("a")
# print(b)


ch = input("Enter a character : ")
# H
"""
if (ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z"):
    print("It is Alphabet")
elif ch >= "0" and ch <= "9":
    print("It is Digit")
else:
    print("Special Symbol")

"""
"""
if (
    ch == "A"
    or ch == "E"
    or ch == "I"
    or ch == "O"
    or ch == "U"
    or ch == "a"
    or ch == "e"
    or ch == "i"
    or ch == "o"
    or ch == "u"
):
    print("Vowel")

elif (ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z"):
    print("Consonent")
elif ch >= "0" and ch <= "9":
    print("It is Digit")
else:
    print("Special Symbol")

"""

"""
if ch in "AEIOUaeiou":
    print("Vowel")
elif (ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z"):
    print("Consonent")
elif ch >= "0" and ch <= "9":
    print("It is Digit")
else:
    print("Special Symbol")

"""

print("Ch :", ch)

if ch >= "A" and ch <= "Z":
    ch = chr(ord(ch) + 32)
elif ch >= "a" and ch <= "z":
    ch = chr(ord(ch) - 32)


print("Ch :", ch)

# time >= 5 and time <= 11:


'''
Input electricity units used and decide rate:

0–100 units → ₹2/unit
101–300 units → ₹3/unit
301–500 units → ₹5/unit
500 units → ₹8/unit


user => 80
Rate -> 80 * 2 -> 160

user -> 350

rate => 100 * 2 + (Unit - 100) * 3
        200 + (150 - 100) * 3
        200 + 50 * 3
        200 + 150 -> 350
        
        
        
'''
