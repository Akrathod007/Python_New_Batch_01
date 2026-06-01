# import random

# print(random.random())
# print(random.randint(10, 20))


import random as r

print(r.random())
print(r.randint(5, 10))
print(r.randrange(1, 5))
print(r.randrange(1, 10, 2))

li = ["Apple", "Banana", "Mango"]

print(r.choice(li))

print(r.choices(li, k=4))

print(r.sample(li, 2))


nums = [1, 2, 3, 4, 5, 1]

r.shuffle(nums)
print(nums)

print(r.uniform(1.1, 2.2))


"""
1. Write a program to generate a 4-digit OTP.

2. Write a program to make Lottery Game :

Generate 5 random numbers (1 - 50).
li = [34,23,45,12,37]

Ask user to guess numbers.
for i in range(1,16):

    no = 55
    match = 1
Check how many matches.

3. Write a program to generate a random HEX color code like #A3F4C1.

4. Write a program to guess the Number Game

randomNo = 1 to 25 (18)

while True:
    no = 16 -> Too Low
    no -> 20 -> To High
    no = 18 -> Break
 


5. Write a program to make Rock Paper Scissors game

com = rock
user = paper

if com == user:
    draw

if (user == "R" and com == "S") or (user == "P" and com == "R") or (user == "S" and com == "p"):
    user win


"""
"""
import math as m

print(m.pi)
print(m.e)
print(m.sqrt(25))
print(m.pow(2, 3))

print(m.ceil(1.2))
print(m.floor(1.2))
print(m.trunc(1.65))

print(round(1.5))
print(m.factorial(5))
print(m.gcd(12, 18))

# 12 -> 1,2,3,4,6,12
# 18 -> 1,2,3,6,9,18
print(m.fabs(-2.4))
print(m.fmod(4.5, 2.3))
print(m.log(10))
print(m.log10(100))
print(m.log2(10))
print(m.sin(90))
print(m.cbrt(27))


import string as s

print(s.ascii_letters)
print(s.ascii_lowercase)
print(s.ascii_uppercase)
print(s.digits)
print(s.hexdigits)
print(s.octdigits)
print(s.punctuation)
print(s.whitespace)


# Check digits in a string :

a = "Name123"
d = 0
for i in a:
    if i in s.digits:
        d += 1

print(d)
"""

# Random Password Generator :
"""
1. Write a program to generate a 4-digit OTP.

2. Write a program to make Lottery Game :

Generate 5 random numbers (1 - 50).
li = [34,23,45,12,37]

Ask user to guess numbers.
for i in range(1,16):

    no = 55
    match = 1
Check how many matches.

3. Write a program to generate a random HEX color code like #A3F4C1.

4. Write a program to guess the Number Game

randomNo = 1 to 25 (18)

while True:
    no = 16 -> Too Low
    no -> 20 -> To High
    no = 18 -> Break
 


5. Write a program to make Rock Paper Scissors game

com = rock
user = paper

if com == user:
    draw

if (user == "R" and com == "S") or (user == "P" and com == "R") or (user == "S" and com == "p"):
    user win


"""

# 1. Write a program to generate a 4-digit OTP.
import random as r

# otp = r.randint(1000, 9999)
# print(otp)

"""
2. Write a program to make Lottery Game :

Generate 5 random numbers (1 - 50).
li = [34,23,45,12,37]

Ask user to guess numbers.
for i in range(1,16):

    no = 55
    match = 1
Check how many matches.

"""
"""
li = []

for i in range(1, 6):
    li.append(r.randint(1, 50))

# print(li)

match = 0
for i in range(1, 11):
    no = int(input("Enter your number : "))
    if no in li:
        match += 1

print("Match Count :", match)

"""

# 3. Write a program to generate a random HEX color code like #A3F4C1.
"""
hexa = "0123456789abcdefABCDEF"
print(r.choice(hexa))

hexColor = "#"

for i in range(1, 7):
    hexColor += r.choice(hexa)

print(hexColor)

"""


# Write a program to guess the Number Game
"""
random = r.randint(1, 25)

while True:
    no = int(input("Enter a number : "))

    if no > random:
        print("Too High")
    elif no < random:
        print("Too Low")
    elif no == random:
        print("Correct Guess")
        break

"""
"""
5. Write a program to make Rock Paper Scissors game

com = rock
user = paper

if com == user:
    draw

if (user == "R" and com == "S") or (user == "P" and com == "R") or (user == "S" and com == "p"):
    user win

"""
"""
li = ["Rock", "Paper", "Scissor"]

com_choice = r.choice(li).lower()

user = input("Enter a Your Choice in Rock Paper Scissor : ").lower()
print("Compuer Choice : ", com_choice)
print("User Choice : ", user)
if com_choice == user:
    print("Draw")
elif (
    (user == "rock" and com_choice == "scissor")
    or (user == "paper" and com_choice == "rock")
    or (user == "scissor" and com_choice == "paper")
):
    print("User Win")
else:
    print("Lose! Computer Win")


"""

import datetime as dt

print(dt.date.today())
print(dt.datetime.now())
d = dt.date(2020, 6, 12)
print(d)

# today = dt.date.today()
today = dt.datetime.now()
print(today.day)
print(today.month)
print(today.year)
print(d.month)
print(d.year)

# print(today.second)
# print(today.minute)
# print(today.hour)
# print(today.microsecond)

print(today.strftime("%d-%m-%y"))
# today = today.strftime("%d-%m-%y")
# print(today)
print(today.strftime("%d-%m-%Y"))

print(today.strftime("%A %a %B %b %H %I %p"))
print(today.strftime("%H:%M:%S.%f"))
print(today.strftime("%j"))
print(today.strftime("%U"))
print(today.strftime("%W"))
print(today.strftime("%c"))
print(today.strftime("%x"))
print(today.strftime("%X"))


today = dt.date.today()
new_date = today + dt.timedelta(days=5)

print(new_date)


d1 = dt.date(2026, 2, 8)
d2 = dt.date(2026, 2, 1)

diff = d1 - d2
print(diff)
print(diff.days)

time_now = dt.datetime.now().time()
print(time_now)


date_string = "08-02-2026"
date_obj = dt.datetime.strptime(date_string, "%d-%m-%Y")

print(date_obj)


# Calculate Days Left for New Year :

