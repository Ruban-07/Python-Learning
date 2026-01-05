# Lesson 14 - Building a Better Calculator:

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operator = input("Enter your operator: ")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1-num2)
elif operator == '*':
    print(num1*num2)
elif operator == '/':
    print(num1/num2)
else:
    print("Enter proper operator symbol")