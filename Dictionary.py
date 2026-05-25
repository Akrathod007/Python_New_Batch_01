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
