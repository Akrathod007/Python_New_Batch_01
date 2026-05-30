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
