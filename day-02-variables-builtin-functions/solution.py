"""Day 02 - Variables, Built-in Functions

Exercises from 30-Days-Of-Python by Asabeneh Yetayeh.
https://github.com/asabeneh/30-Days-Of-Python/tree/master/02_Day_Variables
"""

import math

# Exercises: Level 1
# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# Write a python comment saying 'Day 2: 30 Days of python programming'
# Declare a first name variable and assign a value to it
first_name = "Alex"
# Declare a last name variable and assign a value to it
last_name = "Huaracha"
# Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name
# Declare a country variable and assign a value to it
country = "Peru"
# Declare a city variable and assign a value to it
city = "Lima"
# Declare an age variable and assign a value to it
age = 25
# Declare a year variable and assign a value to it
year = 2023
# Declare a variable is_married and assign a value to it
is_married = False
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = True
# Declare multiple variable on one line
num_one, num_two = 5, 4

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(num_one))
print(type(num_two))

# Using the len() built-in function, find the length of your first name
print(len(first_name))
# Compare the length of your first name and your last name
print(len(last_name))
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle using math pi
area_of_circle = math.pi * 30 ** 2
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * 30
# Take radius as user input and calculate the area.
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is:", area)
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))
print("Your name is", first_name, last_name)
print("You are from", country)
print("You are", age, "years old")
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
