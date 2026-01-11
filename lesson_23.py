# Lesson 23 - Try and Except

try:
    answer = 10/0
    number = int(input("Enter your number: "))
    print(number)

except ZeroDivisionError as error:
    print("ERROR: " + str(error))

except ValueError as error:
    print("ERROR: " + str(error))