"""Day 05 - Lists

Exercises from 30-Days-Of-Python by Asabeneh Yetayeh.
https://github.com/asabeneh/30-Days-Of-Python/tree/master/05_Day_Lists
"""
# Exercises: Day 5
# Exercises: Level 1
# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
items_list = [1, 2, 3, 4, 5, 6]

# Find the length of your list
length = len(items_list)

# Get the first item, the middle item and the last item of the list
first_item = items_list[0]
middle_item = items_list[length // 2]
last_item = items_list[-1]

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Alice", 25, 5.6, "Single", "123 Main St"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)


# Add an IT company to it_companies
it_companies.append("Netflix")
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "Twitter")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
joined_companies = "#;  ".join(it_companies)
print(joined_companies)

# Check if a certain company exists in the it_companies list.
company_exists = "Google" in it_companies
print(company_exists)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(first_three)

# Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

# Slice out the middle IT company or companies from the list
middle = it_companies[len(it_companies) // 2]
print(middle)

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies) // 2)
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_lists = front_end + back_end
print(joined_lists)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = joined_lists.copy()
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)

# Find the median age (one middle item or two middle items divided by two)
length = len(ages)
median_age = (ages[length // 2] + ages[(length - 1) // 2]) / 2
print(median_age)

# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print(average_age)

# Find the range of the ages (max minus min)
age_range = max_age - min_age
print(age_range)

# Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print(min_diff)
print(max_diff)

# Find the middle country(ies) in the countries list (./countries.py)
from countries import countries
# no usar condicionales
middle_countries = countries[len(countries) // 2 - (len(countries) % 2 == 0):len(countries) // 2 + 1]
print(middle_countries)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
half = (len(countries) + 1) // 2
first_half = countries[:half]
second_half = countries[half:]
print(first_half)
print(second_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries_list
print(first)
print(second)
print(third)
print(scandic_countries)
