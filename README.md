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

## List Functions:

To extend a list with an another list, we can use `.extend()`:

```python
lucky_numbers = [7,5,3,1,8]
friends = ["Rohith", "Sanjay", "Akbar", "Deepak"]

friends.extend(lucky_numbers)

print(friends) # Output: ['Rohith', 'Sanjay', 'Akbar', 'Deepak', 7, 5, 3, 1, 8]
```

To Add another Item in the List, we can use `append()`:

```python
friends = ["Rohith", "Sanjay", "Akbar", "Deepak"]

friends.append("Yasif")

print(friends) # Output: ['Rohith', 'Sanjay', 'Akbar', 'Deepak', 'Yasif']
```

To insert a item in a position of list we can use `insert()`:

```python
friends = ["Rohith", "Sanjay", "Akbar", "Deepak"]

friends.insert(1,"Yasif")

print(friends) # Output: ['Rohith', 'Yasif', 'Sanjay', 'Akbar', 'Deepak']
```

To Remove a Item from a list, we can use `remove()`:

```python
friends = ["Rohith", "Yasif", "Sanjay", "Akbar", "Deepak"]

friends.remove("Yasif")

print(friends) # Output: ['Rohith', 'Sanjay', 'Akbar', 'Deepak']
```

To Clear the list, we can use `clear()`:

```python
friends = ["Rohith", "Sanjay", "Akbar", "Deepak"]

friends.clear()

print(friends) # Output: []
```

To Remove Last element in the list, we can use `pop()`:

```python
friends = ["Rohith", "Sanjay", "Akbar", "Deepak", "Yasif"]

friends.pop()

print(friends) # Output: ["Rohith", "Sanjay", "Akbar", "Deepak"]
```

To find an index of an item in the list, we can use `index()`:

```python
friends = ["Rohith", "Sanjay", "Akbar", "Deepak"]

print(friends.index("Akbar")) # Output: 2
```

To find how many time an list item occurs, we can use `count()`:

```python
friends = ["Rohith", "Sanjay", "Akbar", "Sanjay", "Deepak", "Sanjay"]

print(friends.count("Sanjay")) # Output: 3
```

To sort a list in ascending order, we can use `sort()`:

```python
lucky_numbers = [7,5,3,1,8]
friends = ["Rohith", "Sanjay", "Akbar", "Deepak"]

lucky_numbers.sort()
friends.sort()

print(lucky_numbers) # [1, 3, 5, 7, 8]
print(friends) # Output: ['Akbar', 'Deepak', 'Rohith', 'Sanjay']
```

To reverse order of the list, we can use `reverse()`:

```python
friends = ["Rohith", "Sanjay", "Akbar", "Deepak"]

friends.reverse()

print(friends) # Output: ['Deepak', 'Akbar', 'Sanjay', 'Rohith']
```

To copy a list, we can use `copy()`:

```python
friends = ["Rohith", "Sanjay", "Akbar", "Deepak"]

friends2 = friends.copy()

print(friends2) # Output: ['Rohith', 'Sanjay', 'Akbar', 'Deepak']
```

## Tuples:

The `tuples` are similar to `lists`, but `tuples` values are not change, we can't change the value of `tuples` once assigned. Other than that same as `lists`

```python
coordinates = (2,3)

print(coordinates[0]) # Output: 2
```

## Functions:

To write a function in `python`, we need to use `def` keyword. And followed by `def` keyword `function_name` with `()` parentheses and end with `:` colon, from next line with proper indentation, the function begins.

```python
# Function Declaration
def my_wishes():
    print("Happy Morning!")

# Function Calling
my_wishes() # Output: Happy Morning!
```

Passing a parameter in a function:

```python
def my_wishes(name):
    print("Happy Morning " + name + "!")

my_wishes("Ruban") # Output: Happy Morning Ruban!
```

Passing Multiple Parameter in a functions:

```python
def my_wishes(name,age):
    print("Happy Morning " + name + ", you are " + str(age))

my_wishes("Ruban",24) # Output: Happy Morning Ruban, you are 24
```

## Return Statement:

```python
def cube_number(num):
    return num*num*num

result = cube_number(2)
print(result) # Output: 8
```

## If Statements:

```python
is_male = False

if is_male:
    print("You're male!") # if true this will be printed
else:
    print("You're not a male!") # if false this will be printed
```

To check any one condition satisfies, we can use `or` keyword:

```python
is_male = False
is_tall = True

if is_male or is_tall:
    print("You're a tall male!")
else:
    print("You're neither male nor tall!")
```

To check both the conditions satisfies, we can use `and` keyword:

```python
is_male = False
is_tall = True

if is_male and is_tall:
    print("You're a tall male!")
else:
    print("You're neither male nor tall!")
```

Else if Condition for adding more complexity:

```python
is_male = False
is_tall = True

if is_male and is_tall:
    print("You're male!")
elif is_male and not(is_tall):
    print("You're short male!")
elif not(is_male) and is_tall:
    print("You're not male but tall!")
else:
    print("You're neither male nor tall!")

# Output: You're not male but tall!
```

## If Statements & Comparisons:

This function will help use to find the maximum number among the 3 numbers.

```python
def find_max_num(num1,num2, num3):
    if num1>= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3

print(find_max_num(200,302,250))
```

## Building a Better Calculator:

This is the enhanced version of previous calculator, which can get an input of 2 number and the operator to perform operation from the user.

```python
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
```

## Dictionaries:

The `Dictionaries` consists of key value pairs, which will be wrapped in the curly braces and the key should be unique.

```python
monthConversations = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversations.get('ball','Not a valid key')) # Output: Not a valid key
print(monthConversations.get('Sep','Not a valid key')) # Output: September

```

## While Loop:

This is the simple while loop in python.

```python
count = 1

while count <= 10:
    print(count)
    count+=1

print("Loop Completed!")

# Output:
1
2
3
4
5
6
7
8
9
10
Loop Completed!
```

## Building a Guessing Game:

Complex while loop game.

```python
secret_name = "Ruban"
guess_name = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess_name != secret_name and not(out_of_guesses):
    if guess_count < guess_limit:
        guess_name = input("Enter your guess name: ")
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Oops, you Lost the game!")
else:
    print("Wow, you won the game!")
```

## For Loop:

```python
for letter in "Ruban":
    print(letter)

# Output:
R
u
b
a
n
```

```python
cars = ["Bmw","Benz", "Audi", "Rolls Royce"]

for car in cars:
    print(car)

# Output:

Bmw
Benz
Audi
Rolls Royce
```

```python
cars = ["Bmw","Benz", "Audi", "Rolls Royce"]

for car in range(len(cars)):
    print(cars[car])

# Output:
Bmw
Benz
Audi
Rolls Royce
```

```python
for index in range(5):
    if index == 0:
        print("First Iteration!")
    else:
        print("Not a First Iteration!")

# Output:
First Iteration!
Not a First Iteration!
Not a First Iteration!
Not a First Iteration!
Not a First Iteration!
```

## Exponent Function:

```python
def raise_to_power(base_number,power_number):
    result = 1
    for index in range(power_number):
        result = result * base_number
    return result

print(raise_to_power(2,3))
# Output:
8
```

The above function can be achieved by below function:

```python
def raise_to_power_by_exponent(base_number,power_number):
    return print(base_number**power_number)

raise_to_power_by_exponent(2,3)

# Output:
8
```

## 2D Lists and Nested Loops:

2D Lists:

```python
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[1][1])

# Output:
5
```

```python
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in number_grid:
    print(row)

# Output:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
[0]
```

```python
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)

# Output:
1
2
3
4
5
6
7
8
9
0
```

## Build a Translator:

```python
def translate_word(word:str):
    translated_word = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translated_word = translated_word + "G"
            else:
                translated_word = translated_word + "g"
        else:
            translated_word = translated_word + letter
    return translated_word


print(translate_word(input("Enter your word: ")))

# Output:
Enter your word: Rocket
Rgckgt
```

## Comments:

There are single line comment and multi-line in python. The Single line comment is recommend for multi-line comment

```python
#  Single Line Comment

'''
This is
the multi-line
comments
'''
```
