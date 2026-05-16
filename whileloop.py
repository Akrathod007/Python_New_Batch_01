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
