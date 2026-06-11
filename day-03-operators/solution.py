"""Day 03 - Operators

Exercises from 30-Days-Of-Python by Asabeneh Yetayeh.
https://github.com/asabeneh/30-Days-Of-Python/tree/master/03_Day_Operators
"""

# Exercises - Day 3
# Declare your age as integer variable
age = 25

# Declare your height as a float variable
height = 5.9

# Declare a variable that store a complex number
complex_number = 3 + 4j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# Enter length: 5
# Enter width: 3
# The area of the rectangle is 15
# The perimeter of the rectangle is 16
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}")

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# Enter radius: 5
# The area of the circle is 78.5
# The circumference of the circle is 31.400000000000002
pi = 3.14
radius = float(input("Enter radius: "))
area = pi * radius * radius
circumference = 2 * pi * radius
print(f"The area of the circle is {area}")
print(f"The circumference of the circle is {circumference}")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is 2, x-intercept is 1 and y-intercept is -2
slope = 2
x_intercept = 1
y_intercept = -2
print(f"Slope: {slope}, x-intercept: {x_intercept}, y-intercept: {y_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Slope: 2.0, Euclidean distance: 5.656854249492381
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"Slope: {slope}, Euclidean distance: {euclidean_distance}")

# Compare the slopes in tasks 8 and 9.
# The slopes are equal.
if slope == 2:
    print("The slopes are equal.")
else:    print("The slopes are not equal.")

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# y is 0 when x is -3.
x = -3
y = x**2 + 6*x + 9
print(f"When x is {x}, y is {y}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_length = len('python')
dragon_length = len('dragon')
print(f"Length of 'python': {python_length}")
print(f"Length of 'dragon': {dragon_length}")
print(f"Falsy comparison: {python_length < dragon_length}")

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# There is no 'on' in both dragon and python
print(f"'on' in 'python': {'on' in 'python'}")
print(f"'on' in 'dragon': {'on' in 'dragon'}")

# Find the length of the text python and convert the value to float and convert it to string
python_length = len('python')
python_length_float = float(python_length)
python_length_string = str(python_length_float)
print(f"Length of 'python' as float: {python_length_float}")
print(f"Length of 'python' as string: {python_length_string}")

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 10
is_even = (number % 2 == 0)
print(f"{number} is even: {is_even}")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
int_converted = int(2.7)
print(f"Floor division of 7 by 3: {floor_division}")
print(f"Int converted value of 2.7: {int_converted}")
print(f"Are they equal? {floor_division == int_converted}")

# Check if type of '10' is equal to type of 10
print(f"Type of '10': {type('10')}")
print(f"Type of 10: {type(10)}")
print(f"Are they equal? {type('10') == type(10)}")

# Check if int('9.8') is equal to 10
# int_converted = int('9.8')
# print(f"Int converted value of '9.8': {int_converted}")
# print(f"Is it equal to 10? {int_converted == 10}")
# The above code will raise a ValueError because '9.8' cannot be directly converted to an integer. We need to convert it to a float first, then to an integer.
float_converted = float('9.8')
int_converted = int(float_converted)
print(f"Int converted value of '9.8': {int_converted}")
print(f"Is it equal to 10? {int_converted == 10}")

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print(f"Your weekly earning is {weekly_earning}")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds.")

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1, 6):
    print(f"{i} {1} {i} {i**2} {i**3}")
