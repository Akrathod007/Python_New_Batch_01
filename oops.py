# class Car:
#     height = 100
#     weight = 200

#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     def display(self):
#         print(self)
#         print(f"{self.color} and {self.model}")


# c = Car("Black", "Benz")

# print(c)
# print(c.height)
# print(c.weight)
# print(Car.height)
# c.display()

# c2 = Car("White", "Audi")
# c2.display()

# c2.color = "Blue"
# c2.display()
# c.display()

# Car.height = 2000
# print(c.height)
# print(c2.height)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # p1 = Person()
# # p1.name = "Ram"
# # p1.age = 21

# # p2 = Person()
# # p2.name = "Shyam"
# # p2.age = 22

# p1 = Person("Ram", 21)
# p2 = Person("Shyam", 22)

# p3 = Person()


# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(self)
#         print(self.name)


# p1 = Person("Ram")
# p2 = Person("Shyam", 25)

# print(p1.name, p1.age)
# print(p2.name, p2.age)
# p1.display()
# p2.display()


# class Person:
#     def __init__(myobject, name, age):
#         myobject.name = name
#         myobject.age = age

#     def greet(abc):
#         print("Hello, my name is " + abc.name)


# p1 = Person("Emil", 36)
# p1.greet()


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.brand} {self.model}")


# car1 = Car("BenZ", "Maybec", 2020)
# car1.display_info()
# car2 = Car("ABC", "XYZ", 2025)
# car2.display_info()
# del car1.brand
# # car1.display_info()
# car2.display_info()

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return "Hello, " + self.name

#     def welcome(self):
#         message = self.greet()
#         print(message + "! Welcome")


# p1 = Person("Tilak")
# p1.welcome()


# class Person:
#     species = "Human"  # Class property

#     def __init__(self, name):
#         self.name = name  # Instance property


# p1 = Person("Hatori")
# p2 = Person("Doremee")

# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)

# Person.species = "Cartoon"

# print(p1.species)
# print(p2.species)


# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def multiply(self, a, b):
#         return a * b


# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.multiply(4, 7))


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def celebrate_birthday(self):
#         self.age += 1
#         print(f"Happy birthday! You are now {self.age}")

#     def __str__(self):
#         return f"Name :{self.name} and Age : {self.age}"


# p1 = Person("Ram", 25)
# p1.celebrate_birthday()
# p1.celebrate_birthday()
# print(p1)


# class Playlist:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []

#     def add_song(self, song):
#         self.songs.append(song)
#         print(f"Added: {song}")

#     def remove_song(self, song):
#         if song in self.songs:
#             self.songs.remove(song)
#             print(f"Removed: {song}")

#     def show_songs(self):
#         print(f"Playlist '{self.name}':")
#         for song in self.songs:
#             print(f"- {song}")


# my_playlist = Playlist("Favorites")
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Stairway to Heaven")
# my_playlist.show_songs()
# my_playlist.remove_song("Bohemian Rhapsody")
# my_playlist.show_songs()

# my_playlist2 = Playlist("Happy")
# my_playlist2.add_song("ABC")
# my_playlist2.add_song("XYZ")
# my_playlist2.show_songs()
# my_playlist2.remove_song("XYZ")
# my_playlist2.show_songs()


# del my_playlist2.show_songs

# my_playlist2.show_songs()


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def setMarks(self, marks):
        self.__marks = marks

    def getMarks(self):
        return self.__marks


s1 = Student("Ram", 98)

print(s1.name)
# print(s1.__marks)
# s1.setMarks(90)
print(s1.getMarks())


class Animal:

    def eat(self):
        print("Animals eat food")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.eat()
d.bark()


class Father:
    def skill1(self):
        print("Driving")


class Mother:
    def skill2(self):
        print("Cooking")


class Child(Father, Mother):
    def skill3(self):
        print("Playing")


c = Child()
c.skill1()
c.skill2()
c.skill3()


class Grandfather:
    def house(self):
        print("Grandfather's house")


class Father(Grandfather):
    def car(self):
        print("Father's car")


class Son(Father):
    def bike(self):
        print("Son's bike")


s = Son()

s.house()
s.car()
s.bike()


class Animal:
    def eat(self):
        print("Animals eat food")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


d = Dog()
c = Cat()

d.eat()
c.eat()


"""
    Vehicle
     /  \
normal  sprots       
  car     car
    \    /
      Electric 
       car
"""


class Animal:

    def sound(self):
        print("Animals make sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


d = Dog()
d.sound()


class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks


s = Student("Ansh", 95)

print(s.name)
print(s.marks)
