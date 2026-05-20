"""
l1 = [1, 2, 3, 4, 5]
print(l1)
print(type(l1))

l2 = [12, 3.14, True, "Ram"]
print(l2)

l3 = []
print(l3)

l4 = list((1, 2, 3, 4, 5))
print(l4)

"""

"""
l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l5[0])
print(l5[5])
print(l5[-1])

print(l5[-6])

print(l5[0:5])
print(l5[:8])
print(l5[2:])
print(l5[1:8:5])
print(l5[::-1])
print(l5[::-3])

# print(l5[-2:-7])
print(l5[-7:-2])
print(l5[-2:-7:-1])
print(l5[3:-3])
print(l5[-4:2:-1])


a = [1, 2, 3]
b = [4, 5, 6]
c = [1, 2, 3]
d = a
print(a + b)
print(a * 4)

# a[2] = 300
print(a)
print(2 in a)
print(22 in a)
print(22 not in a)
print(2 not in a)

print(a == b)
print(a == c)

print(a is c)
print(a is d)

"""


l7 = [1, 2, 3, 4, 5, 4, 6, 5, 4, 7, 8, 9, 1, 2]

print(l7)

l7.append(200)
print(l7)

l7.insert(4, 500)
print(l7)

l8 = [100, 200, 300]

l7.extend(l8)
print(l7)

print(l7.index(4, 4))
print(l7.index(4, 7, 10))

# print(l7.index(111))

print(sum(l7))
print(max(l7))
print(min(l7))
print(len(l7))

# l7.reverse()
# print(l7)
l7.pop()
print(l7)

l7.pop(6)
print(l7)

# l7.pop(21)
# print(l7)

# l8 = []
# l8.pop()

l7.remove(7)
print(l7)
# l7.remove(4)
# print(l7)

print(l7.count(4))

l9 = l7.copy()
print(l9)
l9[2] = 2000
print(l7)
print(l9)


l9.clear()
print(l9)

# del l9
# print(l9)
