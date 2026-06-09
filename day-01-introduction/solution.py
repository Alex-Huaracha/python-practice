"""Day 01 - Introduction

Exercises from 30-Days-Of-Python by Asabeneh Yetayeh.
https://github.com/asabeneh/30-Days-Of-Python/tree/master/01_Day_Introduction
"""

import math

# Exercise: Level 1
# Check the python version you are using
# python3 --version

# Open the python interactive shell and do the following operations. The operands are 3 and 4.
# addition(+)
print(3 + 9)  # 12
# subtraction(-)
print(3 - 9)  # -6
# multiplication(*)
print(3 * 9)  # 27
# modulus(%)
print(3 % 9)  # 3
# division(/)
print(20 / 3)  # 6.666666666666667
# exponential(**)
print(3**9)  # 19683
# floor division operator(//)
print(20 // 3)  # 6

# Write strings on the python interactive shell. The strings are the following:
# Your name
name = "Alex"
# Your family name
family_name = "Huaracha"
# Your country
country = "Peru"
# I am enjoying 30 days of python
challenge = "I am enjoying 30 days of python"

# Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(["Asabeneh", "Python", "Finland"]))

# Your name
print(name)
# Your family name
print(family_name)
# Your country
print(country)


# Exercise: Level 2
# Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.
# Exercise: Level 3
# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

# Number
print(10)  # Integer
print(9.8)  # Float
print(4 - 4j)  # Complex

# String
print("Hello, Python!")

# Boolean
print(True)
print(False)

# List
print([1, 2, 3, 4, 5])

# Tuple
print((1, 2, 3, 4, 5))

# Set
print({1, 2, 3, 4, 5})

# Dictionary
print({"name": "Alex", "age": 25})

# Find an Euclidean distance between (2, 3) and (10, 8)
point1 = (2, 3)
point2 = (10, 8)
distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
print(distance)
