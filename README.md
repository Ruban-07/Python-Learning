# Python Learning

![Python](https://www.python.org/static/img/python-logo.png)

In this learning we're using python `3.14.2`

## Print Statement

For print somethings we can use `print()` function, which is an in-built function in python. No semicolon needed at the end.

```python
print("Be Happy!")
```

## Variables & Data Types

As we know `Variables` are basically a container to store and maintain a data and the `Data Types` are the type of the data stored.

![Data Types](https://datascientest.com/en/files/2024/06/Python-Variables-1024x585.jpg)

Data Types:

- **`int`** – Represents integer numbers, used for counting and performing arithmetic.

- **`float`** – Represents floating-point numbers (decimals), used for precise calculations.

- **`complex`** – Represents complex numbers, used for mathematical computations involving real and imaginary parts.

- **`str`** – Represents text (string of characters), used for storing and manipulating text.

- **`list`** – Ordered, mutable collection, used for storing sequences of items.

- **`tuple`** – Ordered, immutable collection, used for storing fixed sequences of items.

- **`range`** – Represents a sequence of numbers, used in looping and generating ranges of numbers.

- **`set`** – Unordered, mutable collection of unique items, used for fast membership tests and eliminating duplicates.

- **`frozenset`** – Immutable set, used for immutable collections of unique items.

- **`dict`** – Unordered collection of key-value pairs, used for mapping relationships between data.

- **`bool`** – Represents truth values `True` and `False`, used for conditional statements and logical operations.

- **`bytes`** – Immutable sequence of bytes, used for binary data.

- **`bytearray`** – Mutable sequence of bytes, used for handling binary data that needs modification.

- **`memoryview`** – A view object for binary data, used to manipulate slices of large binary data without copying.

- **`None`** – Represents the absence of a value, used to signify "nothing" or a missing value.

## Working with strings

There are lot of in-built functions are there for string, let's see some of them.

Upper Case:

`.upper()` will help to change the string to uppercase.

```python
print(my_name.upper())
```

Lower Case:

`.lower()` will help to change the string to lowercase.

```python
print(my_name.lower())
```

Check the string is in uppercase or not:

`.isupper()` will help to check whether the string is uppercase or not, it's a boolean function, so it'll return only `True` or `False`.

```python
print(my_name.upper().isupper())
```

Check the string is in lowercase or not:

`.islower()` will help to check whether the string is lowercase or not, it's a boolean function, so it'll return only `True` or `False`.

```python
print(my_name.upper().islower())
```

To Find the length of the string:

`len()` will help to check the length of a string.

```python
print(len(my_name)) # it'll tell the total characters in that string including whitespaces
```

To Replace a character or string:

`replace()` will help us to replace a string with an another string

```python
my_company = "Icore Technology"
print(my_name.replace("Technology","Software"))
```

To change other type to `string`:

`str()` will help us to type conversion to `string`.

```python
my_number = 20
print(my_number) # Output: 20

str(my_number)
print(my_number) # Output: "20"
```

## Working with number

To find the absolute value of a number, it means like positive number.

`abs()` will help to find the absolute value of a number.

```python
my_number = 7.5
print(abs(my_number))
```

To find the value of power:

`pow()` will help us to find the number power.

```python
print(pow(3,2)) #Output: 9
```

To find the large number:

`max()` it'll help us to find the maximum of 2 numbers.

```python
print(max(4,6)) #6
```

To find the small number:

`max()` it'll help us to find the minimum of 2 numbers.

```python
print(min(4,6)) #4
```

To round a decimal number properly:

`round()` will help us to round the number.

```python
print(round(7.7)) # Output: 8
print(round(7.3)) # Output: 7
```

To do more mathematical operations, we can import math and use it like this:

```python
from math import *
```

## Getting Input From Users:

`input()` will help us to get the input from user.

```python
name = input("Enter your name: ")
print("Hello " + name + "!")
```

## Building a Basic Calculator:

```python
num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")

result = num1 + num2
#Input:
#Num1: 7
#Num2: 3
print(result) # Output: 73

result = int(num1) + int(num2)
#Input:
#Num1: 7
#Num2: 3
print(result) # Output: 10

result = int(num1) + int(num2)
#Input:
#Num1: 7.5
#Num2: 3
print(result) # Output: ERROR

result = float(num1) + float(num2)
#Input:
#Num1: 7.5
#Num2: 3
print(result) # Output: 10.5
```

## Mad Libs Game:

```python
color = input("Enter your color: ")
action = input("Enter your action: ")
name = input("Enter your name: ")

print("My car is "+ color + " color")
print(action + " Fast")
print("I Love " + name)
```

## Lists:

```python
friends = ["Rohith", "Sanjay", "Akbar", "Deepak"]

print(friends) # Output: ["Rohith", "Sanjay", "Akbar", "Deepak"]
print(friends[1]) # Output: Sanjay
print(friends[0]) # Output: Rohith
print(friends[-1]) # Output: Deepak
print(friends[1:]) # Output: ["Sanjay", "Akbar", "Deepak"]
print(friends[1:3]) # Output: ["Sanjay", "Akbar"]

friends[2] = "Noorul"
print(friends) # Output: ["Rohith", "Sanjay", "Noorul", "Deepak"]
```
