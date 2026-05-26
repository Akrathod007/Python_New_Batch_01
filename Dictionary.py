user = {"Name": "Ram", "Age": 21, "City": "Ahm", "State": "Guj"}

print(user)
# print(type(user))

# person = dict(name="Shyam", age=22)
# print(person)

# print(user["Name"])
# # print(user["country"])

# print(user.get("Age"))
# print(user.get("Country"))


# del user["State"]
# print(user)

# val = user.pop("Age")
# print(val)
# print(user)

# key, value = user.popitem()
# print(key)
# print(value)

# user.clear()
# print(user)
"""
for key in user:
    # print(key, "->", user.get(key))
    print(key, "->", user[key])


"""
# for key in user.keys():
#     print(key)

# for val in user.values():
#     print(val)


# print(user.keys())
# print(user.values())
# print(user.items())


# for k, v in user.items():
#     print(k, "->", v)


# student = {"name": "Raju", "age": 21}
# print(student.get("name"))
# print(student.get("city", "Not Found"))

# student["age"] = 29
# student["city"] = "Ahm"
# print(student)


# student = {"name": "Raju", "age": 21}
# student.update({"age": 22, "city": "Surat"})
# print(student)

"""
student = {"name": "Raju", "age": 21}
new_student = student.copy()
print(new_student)

new_student["age"] = 30
print(student)
print(new_student)

ns = student
print(ns)

ns["age"] = 30
print(student)
print(ns)


keys = ["math", "science", "english"]
marks = dict.fromkeys(keys, 0)
print(marks)


student = {"name": "Raju"}
print(student.setdefault("age", 20))
print(student)

print(len(marks))

keys = ["Apple", "Banana", "Mango"]
value = [120, 50, 150]

d = dict(zip(keys, value))
print(d)


d2 = {"name": "Ram", "name": "Shyam"}

print(d2)

score_card = {
    "Virat": [70, 89, 45, 67, 88],
    "Dhoni": [80, 67, 90, 45, 33],
    "Sachin": [60, 80, 89, 70, 78],
}

print(score_card["Dhoni"][2])


details = {
    "user": {"name": "Ansh", "age": 21},
    "address": {"city": "Ahm", "State": "Guj"},
}

print(details)
# print(details.get("address")["city"])
print(details.get("address").get("city"))

"""

"""
1. Count Frequency of Characters
word = "python"

freq = {
    "p":1
}

2. Count Frequency of Words
sentence = "python is easy python is powerful"

3. Create Dictionary of Number and Cube
data = {}

data = {
    1:1,
    2:8,
    3:27
}

4. Swap Keys and Values
data = {"a": 1,"b": 2, "c": 3}

5. Find Duplicate Values
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}

6. Create Dictionary From String Length
words = ["python", "java", "ai"]

data = {
    "Python":6
}

7. Count Vowels in Sentence
sentence = "python programming"

8. Create Dictionary of Factorials
data = {
    1:1,
    2:2,
    3:6,
    4:24,
    5:120
}

9. Group Numbers by Positive and Negative
numbers = [10, -5, 7, -2, 0]

data = {
    "positive": [],
    "negative": [],
    "zero": []
}

10. Separate Even and Odd Numbers
numbers = [1, 2, 3, 4, 5, 6]

data = {
    "even": [],
    "odd": []
}

"""

"""
1. Count Frequency of Characters
word = "python"
"""
"""
word = "madam"

freq = {}

for ch in word:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

"""


"""
2. Count Frequency of Words
sentence = "python is easy python is powerful"
"""
"""
sentence = "python is easy python is powerful"

words = sentence.split()
print(words)

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

"""


"""
3. Create Dictionary of Number and Cube
data = {}
"""
"""
no = int(input("Enter a number : "))
data = {}

for i in range(1, no + 1):
    data[i] = i**3

print(data)

"""


"""
4. Swap Keys and Values
data = {"a": 1,"b": 2, "c": 3}
"""
"""
data = {"a": 1, "b": 2, "c": 3}

new_data = {}

for k, v in data.items():
    new_data[v] = k

print(new_data)
"""


"""
5. Find Duplicate Values
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}
"""

"""
data = {"a": 10, "b": 20, "c": 10, "d": 20, "e": 30, "f": 20, "g": 10, "h": 40}

duplicate = []

values = list(data.values())
print(values)

for i in values:
    if values.count(i) > 1 and i not in duplicate:
        duplicate.append(i)

print(duplicate)

"""


"""
6. Create Dictionary From String Length
words = ["python", "java", "ai"]
"""

"""
words = ["python", "java", "ai"]

data = {}

for word in words:
    data[word] = len(word)

print(data)
"""


"""
7. Count Vowels in Sentence
sentence = "python programming"
"""
"""
sentence = "hello python and hello javascript"
data = {}

for ch in sentence:
    if ch in "AEIOUaeiou":
        data[ch] = data.get(ch, 0) + 1

print(data)

"""


"""
8. Create Dictionary of Factorials
"""
"""
no = int(input("Enter a number : "))

data = {}

for i in range(1, no + 1):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j

    data[i] = fact

print(data)

"""


"""
9. Group Numbers by Positive and Negative
numbers = [10, -5, 7, -2, 0]

data = {
    "positive": [],
    "negative": [],
    "zero": []
}

10. Separate Even and Odd Numbers
numbers = [1, 2, 3, 4, 5, 6]

data = {
    "even": [],
    "odd": []
}

"""


numbers = [10, -5, 7, -2, 0]

data = {"positive": [], "negative": [], "zero": []}


for i in numbers:
    if i > 0:
        data["positive"].append(i)
    elif i < 0:
        data["negative"].append(i)
    else:
        data["zero"].append(i)

print(data)
