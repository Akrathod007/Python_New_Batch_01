# for i in range(1, 11):
#     print(i)


# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# i = 1
# sum = 0
# while i <= 10:
#     sum += i

#     i += 1

# print("Sum :", sum)


# no = int(input("Enter a number : "))
"""
5 * 1 = 5
5 * 2 = 10
"""

# i = 1
# while i <= 10:
#     print(no, "*", i, "=", no * i)
#     i += 1

# no = 4567 -> 4
"""
4567 // 10 -> 456, c-> 1
456 // 10 ->  45, c -> 2
45 // 10 -> 4, c -> 3
4 // 10 -> 0, c -> 4

   456
   -------
10|4567
   40
   --
    56
    50
    --
     67
     60
     --
      7
"""
"""
no = int(input("Enter a number : "))

c = 0

while no > 0:
    c += 1
    no = no // 10

print("Count :", c)

"""

# 456 -> 4 + 5 + 6 => 15

# no = int(input("Enter a number : "))
# sum = 0
# mul = 1
# while no > 0:
#     d = no % 10
#     sum += d
#     mul *= d
#     no = no // 10

# print("Sum is :", sum)
# print("Mul is :", mul)

# 123 ->
# if sum == mul:
#     print("Twin Number")
# else:
#     print("Not Twin Number")


# Neon Number
# no -> 9
# s -> 81 -> 9


# 123 -> 321

# no = int(input("Enter a number : "))  # 123
# t = no
# rev = 0

# while no > 0:
#     d = no % 10
#     rev = rev * 10 + d
#     # rev = 0 * 10 + 3 -> 3
#     # rev = 3 * 10 + 2 -> 32
#     # rev = 32 * 10 + 1 -> 321
#     no = no // 10

# print("Reverse Number is", rev)

# if rev == t:
#     print("Palindrome Number")
# else:
#     print("Not Palindrome Number")

# no = 2345646
# fd = 2
# ld = 6
# fd + ld = 8

# Strong Number :
# 145 -> 1! + 4! + 5! -> 1 + 24 + 120 -> 145
"""
no = int(input("Enter a number : "))
t = no
# 145
fact = 1
sum = 0

while no > 0:
    d = no % 10
    fact = 1
    # 145 % 10 -> 5
    # 14 % 10 -> 4
    for i in range(1, d + 1):
        fact = fact * i

    # fact -> 120
    sum = sum + fact
    no = no // 10

if sum == t:
    print("Strong Number")
else:
    print("Not Strong Number")

"""

# Armstrong Number :
# no = int(input("Enter a number : "))
# t = no
# t2 = no
# c = 0
# sum = 0

"""
no = 153

d = 3

1^3 + 5^3 + 3^3 = 1 + 125 + 27 -> 153


12 -> d = 2

1^2 + 2^2 => 1 + 4 -> 5
"""

# print("Number is", no)
# while no > 0:
#     c += 1
#     no = no // 10

# print("Count is", c)

# while t > 0:
#     d = t % 10
#     sum = sum + d**c
#     t = t // 10

# print("Sum is", sum)

# if sum == t2:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")


# for i in range(1, 11):
#     print(i)
#     if i == 5:
#         break


# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)


# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i)
#     # i += 1


# while True:
#     no = int(input("Enter a number or -1 for exit : "))

#     if no == -1:
#         break
#     print(no)


totalBill = 0

while True:

    print("------Hotel Menu------")
    print("1 -> Gujrati")
    print("2 -> South Indian")
    print("3 -> Punjabi")
    print("4 -> Chinese")
    print("5 -> Kathiyawadi")
    print("6 -> Exit")
    ch1 = int(input("Enter Your Choice : "))
    if ch1 == 6:
        break
    match ch1:
        case 1:
            print("You Selected Gujrati")
            print("1 -> Thepla")
            print("2 -> Fafda-Jalebi")
            print("3 -> Dal Dhokli")
            print("4 -> Khichdi Kadhi")
            print("5 -> Undhiyu")
            ch2 = int(input("Enter Your Choice in Gujrati : "))
            match ch2:
                case 1:
                    print("You Selected Thepla")
                case 2:
                    print("You Selected Fafda-Jalebi")
                case 3:
                    print("You Selected Dal Dhokli")
                case 4:
                    print("You Selected Khichdi Kadhi")
                case 5:
                    print("You Selected Undhiyu")

            qty = int(input("How much do you want : "))
            if ch2 == 1:
                total = qty * 20
                print("Thepla :", qty, "* 20 =", total)
            elif ch2 == 2:
                total = qty * 50
                print("Fafda-Jalebi :", qty, "* 50 =", total)
            elif ch2 == 3:
                total = qty * 80
                print("Dal Dhokli :", qty, "* 80 =", total)

            elif ch2 == 4:
                total = qty * 120
                print("Khichdi Kadhi :", qty, "* 120 =", total)

            elif ch2 == 5:
                total = qty * 100
                print("Undhiyu :", qty, "* 100 =", total)

            totalBill += total

        case 2:
            print("You Selected South Indian")
        case 3:
            print("You Selected Punjabi")
        case 4:
            print("You Selected Chinese")
        case 5:
            print("You Selected Kathiyawadi")

print("Total Bill is", totalBill)
