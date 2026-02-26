Sets in Python:
A set is a collection of unique elements.
Sets are unordered and do not allow duplicate values.
syntax:
set_name = {value1, value2, value3}
Example:
numbers = {15, 26, 37, 49}
print(numbers)

output:
{15, 26, 37, 49}

Duplicated values are removed:
numbers = {5,6,8,8,9,10,10,13,13,14}
print(numbers)
output:
{5,6,8,9,14}

Add element:
numbers.add(5)

Remove element:
numbers.remove(3)

Set element:
A = {1, 2, 3}
B = {3, 4, 5}

Union: A | B
Intersection: A & B
Difference: A - B
