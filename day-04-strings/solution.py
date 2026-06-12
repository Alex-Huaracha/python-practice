"""Day 04 - Strings

Exercises from 30-Days-Of-Python by Asabeneh Yetayeh.
https://github.com/asabeneh/30-Days-Of-Python/tree/master/04_Day_Strings
"""

# Exercises - Day 4
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
concatenated_string = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4
print(concatenated_string)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string5 = 'Coding'
string6 = 'For'
string7 = 'All'
concatenated_string2 = string5 + ' ' + string6 + ' ' + string7
print(concatenated_string2)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
print("Python for Everyone".replace("Everyone", "All"))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.
print(company[-1])

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
print("Python For Everyone".split()[0][0] + "For" + "Everyone"[0])
# print("Python For Everyone".split())
# print("Python For Everyone".split()[0])
# print("Python For Everyone".split()[0][0])

# Create an acronym or an abbreviation for the name 'Coding For All'.
print("Coding For All".split()[0][0] + "For" + "All"[0])

# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind("l"))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word = "because"
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index(word))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex(word))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.index(word):sentence.rindex(word) + len(word)])

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find(word))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.find(word):sentence.rfind(word) + len(word)])

# Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

# Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
new_company = '   Coding For All      '
print(new_company.strip())

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = " # ".join(libraries)
print(joined_libraries)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
sentences = "I am enjoying this challenge.\nI just wonder what is next."
print(sentences)

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
num1 = 8
num2 = 6
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
