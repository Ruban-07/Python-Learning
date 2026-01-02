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
