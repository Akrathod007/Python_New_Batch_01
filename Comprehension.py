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

evenOdd = []

for i in range(1, 11):
    if i % 2 == 0:
        evenOdd.append("Even")
    else:
        evenOdd.append("Odd")

print(evenOdd)

# evenOdd2 = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 11)]
# li = [34, 234, 456, 123, 67, 234, 78, 23, 44, 55, 11]
# evenOdd2 = ["Even" if i % 2 == 0 else "Odd" for i in li]
# print(evenOdd2)


# nums = [10, -20, 0, 34, 56, -23, -45, 0, 0, 26]


# posNegZero = ["Pos" if i > 0 else "Neg" if i < 0 else "zero" for i in nums]
# print(posNegZero)

marks = [90, 98, 78, 85, 45, 67, 75, 30, 40]

grade = [
    (
        "A"
        if i >= 90
        else (
            "B"
            if i >= 80
            else "C" if i >= 70 else "D" if i >= 60 else "E" if i >= 50 else "Fail"
        )
    )
    for i in marks
]

print(grade)


c = [10, 45, 23, 67, 30]
# f = c * 1.8 + 32
f = [i * 1.8 + 32 for i in c]
print(f)


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
