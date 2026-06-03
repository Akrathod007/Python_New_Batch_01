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


try:
    d = {"name": "Ram"}
    print(d["age"])
except:
    print("Error")
