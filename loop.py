# for i in range(1, 11):
#     print(i)

# for i in range(1, 12, 5):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# for i in range(10, 0, -3):
#     print(i)

# sum = 0
# for i in range(1, 11):
#     if i == 10:
#         print(i, end=" ")
#     else:
#         print(i, end=" + ")
#     sum += i

# print("=", sum)

# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

# print("Hello", end=" ")
# print("Bye")


# Factorial
# 5! => 5 * 4 * 3 * 2 * 1

# 3! => 3 * 2 * 1

# no = int(input("Enter a number : "))
# fact = 1
# for i in range(1, no + 1):
#     fact = fact * i

# for i in range(no, 0, -1):
#     fact *= i

# print("Fact :", fact)

# Power
# base = 2
# exponent = 4

# 2^6 -> 2 * 2 * 2 * 2 * 2 * 2

# b = int(input("Enter a base : "))
# e = int(input("Enter a exponent : "))

# result = 1

# for i in range(1, e + 1):
#     result = result * b

# print(b, "^", e, "=", result)


# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15

# no = int(input("Enter a number : "))

# for i in range(1, 11):
#     print(no, "*", i, "=", no * i)


# 1 1 2 3 5 8
"""
a = 1
b = 1

c = a + b -> 2
a = b -> 1
b = c -> 2

c = a + b -> 3
a = b -> 2
b = c -> 3

"""

# 6
# no = int(input("Enter a number : "))
# a = 1
# b = 1
# print(a, end=" ")
# print(b, end=" ")

# for i in range(2, no):
#     c = a + b
#     print(c, end=" ")
#     a = b
#     b = c

# Prime Number :

# 5 -> 1 and 5
# 7 -> 1 and 7
# 9 -> 1, 3, and 9

"""
5 -> 
5 % 1 - 0 
5 % 2 - 1
5 % 3 - 2
5 % 4 - 1
5 % 5 - 0

6 ->
 6 % 2 -> 0
 
 5 ->
  5 % 2 -> 1
  5 % 3 -> 2
  5 % 4 -> 1
  
"""


# no = int(input("Enter a number : "))
"""
f = 0

for i in range(1, no + 1):
    if no % i == 0:
        f += 1


if f == 2:
    print("Prime")
else:
    print("Not Prime")
"""
"""
f = 1

for i in range(2, no):
    if no % i == 0:
        f = 0
        break

if f == 1:
    print("Prime")
else:
    print("Not Prime")

"""

# 6 -> 1,2,3,6
"""
no = int(input("Enter a number : "))

sum = 0

for i in range(1, no):
    if no % i == 0:
        sum += i

if sum == no:
    print("Perfect Number")
else:
    print("Not Perfect Number")
"""


# for i in range(1, 6): #i-> 1 -> 2
#     for j in range(1, 4): #j-> 1 -> 2 -> 3 -> 4
#         print("i :", i, " | j :", j)


"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

# for i in range(1, 6):
#     for j in range(1, 6):
#         print("*", end=" ")
#     print()


"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""


# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, end=" ")
#     print()


"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end=" ")
#     print()

"""
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
"""


# for i in range(1, 6):
#     x = chr(i + 64)
#     for j in range(1, 6):
#         print(x, end=" ")
#     print()


"""
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
"""
# for i in range(1, 6):
#     for j in range(1, 6):
#         x = chr(j + 64)
#         print(x, end=" ")
#     print()

# x = chr(65)
# print(x)

# x = ord("a")
# print(x)


"""
*
* *
* * *
* * * *
* * * * *

1 2 3 4 5
1             1
0 1           2
1 0 1         3
0 1 0 1       4
1 0 1 0 1     5
"""

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("* ", end="")
#     print()

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if (i + j) // 2 * 2 == (i + j):
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()


# 10 // 2 -> 5 * 2 -> 10 == 10
# 11 // 2 -> 5 * 2 -> 10 == 11
# / 5 / 2 -> 2.5
# // -> 5 // 2 -> 2
# ** -> 5 ** 2 -> 5 ^ 2 -> 25


"""
1 2 3 4 5
* * * * * 1
*       * 2
*       * 3
*       * 4
* * * * * 5
"""

# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or i == 5 or j == 1 or j == 5:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


"""
12345
*   *  1
 * *   2
  *    3 
 * *   4
*   *  5
"""

# no = int(input("Enter a number : "))


# for i in range(1, no + 1):
#     for j in range(1, no + 1):
#         if i == j or (i + j) == no + 1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


"""
1
A B
1 2 3
A B C D
1 2 3 4 5


        *
      * *
    * * *
  * * * *
* * * * *


        *
       * *
      * * *
     * * * *
    * * * * *        
    
    

        *
       ***
      *****
     *******
    *********    
"""

# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()


# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print("* ", end="")
#     print()


"""

        *
       ***
      *****
     *******
    *********    

"""
# ns = 1
# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end="")
#     for j in range(1, ns + 1):
#         print("*", end="")
#     ns = ns + 2
#     print()


# 1 + 3 + 5 + 7 + 9
# 2*i - 1
# i -> 1
# 2 * 1 - 1 => 2 - 1 -> 1

# i = 2
# 2 * 2 - 1 -> 4 - 1 -> 3


# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end="")
#     for j in range(1, 2 * i):
#         print("*", end="")
#     print()


"""
    1
   123
  12345
 1234567   
123456789

    1
   121
  12321
 1234321
123454321
    
"""

"""
    *
   * *
  *   *
 *     *
*********    


1 + 3 + 5 + 7 + 9

2 * i - 1
2 * 1 - 1 -> 1
2 * 2 - 1 -> 3
2 * 3 - 1 -> 5
"""
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()
