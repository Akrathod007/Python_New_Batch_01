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


"""


# l7 = [1, 2, 3, 4, 5, 4, 6, 5, 4, 7, 8, 9, 1, 2]

# # for i in range(len(l7)):
# #     print(i, "->", l7[i])

# for i in l7:
#     print(i)


"""
1. Find Even and Odd Numbers from a List
l1 = [1,2,3,4,5,6,7,8,9,10]
odd = [1,3,5,7,9]
even = [2,4,6,8,10]
"""
"""
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
even = []

for i in l1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even :", even)
print("Odd :", odd)

"""

"""
2. Remove Duplicates from a List
l1 = [1,2,3,1,2,4,5,3,2]
output = result = [1,2,3,4,5]
"""


"""
l1 = [1, 2, 3, 1, 2, 4, 5, 3, 2]
unique = []

for i in l1:
    if i not in unique:
        unique.append(i)

print("Unique :", unique)

"""


"""
3. Find Common Elements Between Two Lists
l1 = [1,2,3,4]
l2 = [3,4,5,6]

result = [3,4]
"""

"""
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
result = []
for i in l1:
    if i in l2:
        result.append(i)

print("Result :", result)

"""

"""

4. Remove All Even Numbers from a List
l1 = [1,2,3,4,5,6]
result = [1,3,5]
"""

"""
l1 = [1, 2, 3, 4, 5, 6]
result = []

for i in l1:
    if i % 2 != 0:
        result.append(i)

print("Result :", result)

"""

"""
5. Find Elements Present in One List but Not in the Other
l1 = [1,2,3,4]
l2 = [3,4,5,6]

result = [1,2,5,6]
"""

"""
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]

result = []

for i in l1:
    if i not in l2:
        result.append(i)

for i in l2:
    if i not in l1:
        result.append(i)

print("Result :", result)

"""

"""
6. Check if a List is a Palindrome
l1 = [1,2,3,2,1]
rev = [1,2,3,2,1]
"""


"""
l1 = [1, 2, 3, 2, 1, 6]
rev = []

for i in range(len(l1) - 1, -1, -1):
    rev.append(l1[i])

print(l1)
print(rev)

if l1 == rev:
    print("Palindrome List")
else:
    print("Not Palindrome List")

"""

"""
7. Find All Unique Elements in a List
l1 = [1,2,3,1,2,4,5,3,2]
result = [4,5]
"""


"""
l1 = [1, 2, 3, 1, 2, 4, 5, 3, 2]

result = []

for i in l1:
    if l1.count(i) == 1:
        result.append(i)

print("Result :", result)

"""

"""
8. Move All Zeros to the End 
l1 = [1,0,0,2,3,0,2]

result = [1,2,3,2,0,0,0]
"""

l1 = [1, 0, 0, 2, 3, 0, 2]

result = []

for i in l1:
    if i != 0:
        result.append(i)

zeroCount = l1.count(0)

for i in range(1, zeroCount + 1):
    result.append(0)

print(result)
