"""

try:
    x = 10 / 0
except:
    print("Error!")

print("Hello")


try:
    print("Start")
    # print(10 / 0)
    x = int("Hello")
    print("End")
except:
    print("Error Found")

print("Program Continues")

"""

"""
try:
    num = int(input("Enter Number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Enter valid integer")

"""
# try:
#     num = int(input("Enter Number: "))
#     print(10 / num)

# except (ValueError, ZeroDivisionError):
#     print("Invalid Input")


# try:
#     x = 10 / 0

# except Exception as e:
#     print("Error:", e)


# try:
#     num = int(input("Enter Number: "))
#     result = 10 / num

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result =", result)


# try:
#     print(10 / 0)

# except:
#     print("Error")

# finally:
#     print("Always Executes")


# try:
#     d = {"name": "Ram"}
#     print(d["age"])
# except:
#     print("Error")


# age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative")

# print("Valid Age")


# balance = 500
# withdraw = 1000

# try:
#     if withdraw > balance:
#         raise ValueError("Insufficient Balance")
# except ValueError as e:
#     print("Error", e)


class InvalidMarksError(Exception):
    pass


marks = -10

# if marks < 0:
#     raise InvalidMarksError("Marks cannot be negative")

"""
try:
    if marks < 0:
        raise InvalidMarksError("Marks cannot be negative")

except InvalidMarksError as e:
    print("Error : ", e)


try:
    print("Outer Try")

    try:
        print(10 / 0)

    except ZeroDivisionError:
        print("Inner Except: Cannot divide by zero")

except:
    print("Outer Except")


try:
    print("Outer Try")

    try:
        num = int("abc")

    except ZeroDivisionError:
        print("Inner Except")

except ValueError:
    print("Outer Except: Invalid Number")

"""


try:
    file = open("data.txt")

    try:
        data = int(file.read())
        print(data)

    except ValueError:
        print("File contains invalid data")

    finally:
        file.close()
        print("File Closed")

except FileNotFoundError:
    print("File Not Found")
