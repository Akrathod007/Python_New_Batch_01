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


t = 101, "Ram", 98.98
print(t)

sid, name, marks = t
print(sid)
print(name)
print(marks)
