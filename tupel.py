"""

t1 = (1, 2, 3, 4)
print(t1)

t2 = (1, 1.2, "Hello", True)
print(t2)

t3 = ()
print(t3)

t4 = tuple([1, 2, 3, 4])
print(t4)

print(type(t4))

li = list(t4)
print(li)
print(type(li))

print(t4[0])
print(t4[-1])
print(t4[:3])

# t4[0] = 100
# print(t4)

t5 = 1, 2, 3, 4, 2, 5, 6, 2
print(t5)
print(type(t5))


t6 = (10,)
print(t6)
print(type(t6))

t7 = t5 + t6
print(t7)

print(t5 * 3)

print(2 in t5)
print(22 in t5)
print(2 not in t5)
print(22 not in t5)

print(len(t5))
print(max(t5))
print(min(t5))
print(sum(t5))
print(t5.count(2))
print(t5.index(2, 3, 7))


t = 101, "Ram", 98.98, 234, 234, 234
print(t)

sid, name, *other = t
print(sid)
print(name)
print(other)
print(type(other))


t8 = (45, 23, 4, 23, 6, 85, 25, 67)
print(t8)

print(sorted(t8, reverse=True))

print(tuple(sorted(t8)))

"""

# li = [34, 56, 22, 67, 12, 39, 31]

"""
        34, 56, 22, 67, 12, 39, 31

pass
  sub1 : 34, 56, 22, 67, 12, 39, 31
  sub2 : 34, 22, 56, 67, 12, 39, 31
  sub3 : 34, 22, 56, 67, 12, 39, 31
  sub4 : 34, 22, 56, 12, 67, 39, 31
  sub5 : 34, 22, 56, 12, 39, 67, 31
  sub6 : 34, 22, 56, 12, 39, 31, 67

pass2
    sub1 : 22,34,56,12,39,31,67
    sub2 : 22,34,56,12,39,31,67
    sub3 : 22,34,12,56,39,31,67
    sub4 : 22,34,12,39,56,31,67
    sub5 : 22,34,12,39,31,56,67


"""
# li = [34, 56, 22, 67, 12, 39, 31]
li = [1, 2, 3, 4, 5, 6, 7]
c = 0
excg = True
for i in range(len(li) and excg == True):
    excg = False
    for j in range(len(li) - 1 - i):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]
            excg = True
        c += 1

print("Count :", c)
print(li)
