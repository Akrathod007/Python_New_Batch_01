# li = []

# for i in range(1, 11):
#     li.append(i**2)

# print(li)

# square = [i**2 for i in range(1, 11)]
# print(square)

# cube = [i**3 for i in range(1, 11)]
# print(cube)

"""
even = []

for i in range(1, 11):
    if i % 2 == 0:
        even.append(i)

print(even)


even2 = [i for i in range(1, 11) if i % 2 == 0]

print(even2)

"""

# evenOdd = []

# for i in range(1, 11):
#     if i % 2 == 0:
#         evenOdd.append("Even")
#     else:
#         evenOdd.append("Odd")

# print(evenOdd)

# evenOdd2 = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 11)]
# li = [34, 234, 456, 123, 67, 234, 78, 23, 44, 55, 11]
# evenOdd2 = ["Even" if i % 2 == 0 else "Odd" for i in li]
# print(evenOdd2)


# nums = [10, -20, 0, 34, 56, -23, -45, 0, 0, 26]


# posNegZero = ["Pos" if i > 0 else "Neg" if i < 0 else "zero" for i in nums]
# print(posNegZero)

# marks = [90, 98, 78, 85, 45, 67, 75, 30, 40]

# grade = [
#     (
#         "A"
#         if i >= 90
#         else (
#             "B"
#             if i >= 80
#             else "C" if i >= 70 else "D" if i >= 60 else "E" if i >= 50 else "Fail"
#         )
#     )
#     for i in marks
# ]

# print(grade)


# c = [10, 45, 23, 67, 30]
# # f = c * 1.8 + 32
# f = [i * 1.8 + 32 for i in c]
# print(f)


"""
Task 1 : Positive → number, Negative → 0

Input: [-3, 5, -1, 7]
Output: [0, 5, 0, 7]

Task 2 : Greater than 10 → "Big", else "Small"

Input: [5, 15, 8, 20]
Output: ["Small", "Big", "Small", "Big"]

Task 3 :Square if Even, Cube if Odd

Input: [1,2,3,4]
Output: [1,4,27,16]

Task 4 : Marks → "Pass" if ≥ 40 else "Fail"

Input: [35, 50, 90, 20]
Output: ["Fail", "Pass", "Pass", "Fail"]
"""


"""

no -> 10

li = []


"""

# no = int(input("how many elements do you want : "))
# li = []

# for i in range(1, no + 1):
#     li.append(int(input("Enter a value : ")))

# print(li)


# l2 = [int(input("Enter a value : ")) for i in range(1, no + 1)]
# print(l2)


# r = int(input("Enter a row : "))
# c = int(input("Enter a column"))

"""
li = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
"""
# ol = []
# for i in range(1, r + 1):
#     il = []
#     for j in range(1, c + 1):
#         no = int(input("Enter a number : "))
#         il.append(no)
#         # [2,3,4]
#     ol.append(il)

# print(ol)


# l2 = [
#     [int(input("Enter a number : ")) for j in range(1, c + 1)] for i in range(1, r + 1)
# ]

# print(l2)


# s = {i * i for i in range(1, 11)}
# print(s)

# s2 = {i * i for i in range(1, 11) if i % 2 == 0}
# print(s2)

# li = [325, 214, 46, 24, 66, 77, 89, 34]
# s3 = {"even" if i % 2 == 0 else "Odd" for i in li}
# print(s3)


# d = {i: i * i for i in range(1, 11)}
# print(d)

# d = {i: i * i for i in range(1, 11) if i % 2 == 0}
# print(d)

# d2 = {i: "Even" if i % 2 == 0 else "odd" for i in range(1, 11)}
# print(d2)

"""
1. Create a dictionary from 1 to 10, but include only even numbers as keys and their cubes as values.

2. Given a list of words, create a dictionary where key = word and value = length.

3. Create a dictionary from 1 to 10:

Even → "Even"
Odd → "Odd"

4. Swap keys and values of a dictionary.

5. Create a dictionary using two lists.

keys = ["name", "age", "city"]
values = ["Ram", 11, "Surat"]

6. Count frequency of each character in a string.


"""

# 2. Given a list of words, create a dictionary where key = word and value = length.

# words = ["Apple", "Banana", "Mango", "Kiwi", "Watermelon"]

# # li = {w: len(w) for w in words}
# li = {w: w[::-1] for w in words}
# print(li)

# 4. Swap keys and values of a dictionary.

# d = {"a": 1, "b": 2, "c": 3}

# d1 = {v: k for k, v in d.items()}
# print(d1)


"""

5. Create a dictionary using two lists.

keys = ["name", "age", "city"]
values = ["Ram", 11, "Surat"]
"""
"""

keys = ["name", "age", "city"]
values = ["Ram", 11, "Surat"]


d = {keys[i]: values[i] for i in range(len(keys))}
print(d)

"""

# 6. Count frequency of each character in a string.

s = "Mississippi"

d = {ch: s.count(ch) for ch in s}
print(d)
