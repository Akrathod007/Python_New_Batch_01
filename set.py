"""

s = {}
print(s)
print(type(s))

s = set()
print(s)
print(type(s))

s1 = {1, 2, 3, 4, 5}
print(s1)

s2 = {1, 3.14, "Hello", False, "Bye"}
print(s2)

# print(s2[0]) -> Error

li = [1, 2, 3, 2, 3, 4, 5, 4, 3]

s3 = set(li)
s4 = list(s3)
print(s4)

# s5 = {1, 2, [1, 2, 3]}
# print(s5)
# Error


s6 = {1, 2, (1, 2, 3)}
print(s6)

s7 = {"Raju", "Ram", "Shyam", "Manan", "Raj"}
print(s7)

s7.add("Piya")
print(s7)

s7.add(10)
print(s7)

s7.remove("Manan")
print(s7)

s7.discard("Ra")
print(s7)

elm = s7.pop()
print(elm)
print(s7)

s7.clear()
print(s7)

"""

"""
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a | b
print(c)
# print(a.union(b))
a.union(b)
print(a)

print(a & b)
print(a.intersection(b))

print(a - b)
print(b - a)
print(a.difference(b))

print(a ^ b)
print(a.symmetric_difference(b))

"""
"""

a = {1, 2}
b = {1, 2, 3}

print(a <= b)
print(a.issubset(b))
print(b.issubset(a))

print(a >= b)
print(a.issuperset(b))
print(b.issuperset(a))

print(a.isdisjoint(b))

x = {1, 2}
y = {3, 4}
print(x.isdisjoint(y))

"""

a = {1, 2, 3}
b = {3, 4, 5}
a.update(b)
print(a)

# a.intersection_update(b)
# print(a)

# a.difference_update(b)
# print(a)

a.symmetric_difference_update(b)
print(a)


# s8 = frozenset({1, 2, 3})
# s8 = frozenset([1, 2, 3])
s8 = frozenset((1, 2, 3, 4))
print(s8)

s8.add(10)
