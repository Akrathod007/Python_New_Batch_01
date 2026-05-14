"""
day = int(input("Enter a day between 1 to 7 : "))

match day:
    case 1:
        print("MON")
    case 2:
        print("TUE")
    case 3:
        print("WED")
    case 4:
        print("THU")
    case 5:
        print("FRI")
    case 6:
        print("SAT")
    case 7:
        print("SUN")
    case _:
        print("Invalid Day Number")

"""

"""
month = int(input("Enter a month number : "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 Days")
    case 2:
        print("28 or 29 Days")
    case 4 | 6 | 9 | 11:
        print("30 Days")

"""

# ch = input("Enter a character : ")

# match ch:
#     case "A" | "E" | "I" | "O" | "U" | "a" | "e" | "i" | "o" | "u":
#         print("It is vowel")
#     case _:
#         print("It is not vowel")

# no = int(input("Enter a number : "))
"""
match no % 2:
    case 0:
        print("Even")
    case 1:
        print("Odd")

"""

"""
match no:
    case n if n % 2 == 0:
        print(f"{n} is Even")
    case n if n % 2 != 0:
        print(f"{n} is Odd")

"""
# name = "Doremon"
# age = 1

# print("Name :", name, "Age :", age)
# print(f"Name : {name} and age : {age}")


print("------Hotel Menu------")
print("1 -> Gujrati")
print("2 -> South Indian")
print("3 -> Punjabi")
print("4 -> Chinese")
print("5 -> Kathiyawadi")

ch1 = int(input("Enter Your Choice : "))
match ch1:
    case 1:
        print("You Selected Gujrati")
        print("1 -> Thepla")
        print("2 -> Fafda-Jalebi")
        print("3 -> Dal Dhokli")
        print("4 -> Khichdi Kadhi")
        print("5 -> Undhiyu")
        ch2 = int(input("Enter Your Choice in Gujrati : "))
        match ch2:
            case 1:
                print("You Selected Thepla")
            case 2:
                print("You Selected Fafda-Jalebi")
            case 3:
                print("You Selected Dal Dhokli")
            case 4:
                print("You Selected Khichdi Kadhi")
            case 5:
                print("You Selected Undhiyu")
    case 2:
        print("You Selected South Indian")
    case 3:
        print("You Selected Punjabi")
    case 4:
        print("You Selected Chinese")
    case 5:
        print("You Selected Kathiyawadi")
