# add = lambda a, b: a + b

# print(add(20, 10))

# mul = lambda a, b: a * b
# print(mul(10, 20))


# def evenOdd(no):
#     if no % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# print(evenOdd(10))
# print(evenOdd(11))

"""
evenOdd2 = lambda no: "Even" if no % 2 == 0 else "Odd"

print(evenOdd2(19))
print(evenOdd2(18))


pos_neg_zero = lambda n: "pos" if n > 0 else "neg" if n < 0 else "zero"

print(pos_neg_zero(10))
print(pos_neg_zero(-10))
print(pos_neg_zero(0))

"""

"""
login = lambda user, pwd: (
    "Admin Login"
    if user == "Admin" and pwd == "007"
    else "User Login" if user == "User" and pwd == "123" else "Invalid Login"
)


print(login("Admin", "007"))
print(login("User", "123"))
print(login("Admin", "123"))

"""


# nums = [1, 2, 3, 4, 5]

"""
def square(x):
    return x * x


result = list(map(square, nums))
print(result)

"""

# result = list(map(lambda x: x * x, nums))
# print(result)

"""
li = [23, 56, 11, 26, 78, 89, 67]

evenOdd = list(map(lambda n: "Even" if n % 2 == 0 else "Odd", li))
print(evenOdd)

odd = list(filter(lambda x: x % 2 == 1, li))
# odd = list(filter(lambda x: True if x % 2 == 1 else False, li))
print(odd)

"""


from functools import reduce

# nums = [1, 2, 3, 4, 5]

# total = reduce(lambda a, b: a + b, nums, 10)
# print(total)

# product = reduce(lambda a, b: a * b, nums, 10)
# print(product)


'''
Map Task :
"""
Create a list of numbers and use map() to find squares of all numbers.

Create a list of numbers and use map() to convert all numbers into strings.

Given a list of temperatures in Celsius, use map() to convert them into Fahrenheit.

Create a list of names and use map() to convert all names into uppercase.

Given a list of strings, use map() to find the length of each string.

Create a list of numbers and use map() to add 10 to every element.

Given a list of words, use map() to reverse each word.

Create a list of prices and use map() to add 18% GST to every price.

Create a list of integers and use map() to check whether each number is even or odd.
"""

Filter Task :

1. Filter Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

2. Filter Odd Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

3. Filter Positive Numbers
numbers = [-5, 10, -2, 8, 0]

4. Filter Names Starting With A
names = ["Akshay", "Rahul", "Amit", "Karan"]

5. Filter Strings With Length More Than 5
words = ["apple", "banana", "kiwi", "mango"]

6. Filter Vowels From List
letters = ['a', 'b', 'e', 'f', 'i']

7. Filter Palindrome Words
words = ["madam", "python", "level", "code"]

8. Filter Uppercase Words
words = ["HELLO", "Python", "WORLD", "Code"]

9. Filter Alphabet Characters
data = ['A', '1', 'B', '9', 'C']

10. Filter Strings Containing Letter "a"
words = ["apple", "mango", "berry", "banana"]


Reduce Task :

1. Concatenate Strings
words = ["Python", "is", "awesome"]

2. Reverse a String
word = "python"

3. Find Total Digits in List
numbers = [123, 45, 6789]

4. Find Highest Marks
marks = [45, 78, 90, 66, 88]

5. Count Total Words Length
words = ["python", "java", "c"]




1. Square Even Numbers and Find Sum

2. Sum of Cubes of Positive Numbers

3. Find Sum of Squares of Odd Numbers

4. Find Largest Square of Even Numbers

5. Reverse Long Words and Join
Filter words whose length is greater than 4.

'''


"""
1. Square Even Numbers and Find Sum
"""

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
even = list(filter(lambda x: x % 2 == 0, li))
print(even)

evenSquare = list(map(lambda x: x * x, even))
print(evenSquare)

finalSum = reduce(lambda a, b: a + b, evenSquare)
print(finalSum)

"""

finalSum = reduce(
    lambda a, b: a + b,
    list(map(lambda x: x * x, list(filter(lambda x: x % 2 == 0, li)))),
)

print(finalSum)


li = [1, 2, 3, 4, 7, 5, 6]

maxNum = reduce(lambda x, y: x if x > y else y, li)
minNum = reduce(lambda x, y: x if x < y else y, li)
print(maxNum)
print(minNum)
