Module:
A module is a Python file that contains functions, variables, or classes that can be reused in other programs.
Example: math

Using a Module

Example using the math module:

import math
print(math.sqrt(36))
print(math.factorial(5))

Output
6
120

Import Specific Function
Instead of importing everything:

from math import sqrt

print(sqrt(49))

Output:
7


Using Random Module
import random

print(random.randint(1, 10))

This generates a random number between 1 and 10.

 Creating Your Own Module

my_module.py

def greet(name):
    print("Hello", name)

import my_module

my_module.greet("Sumitha")

Output:

Hello Sumitha

 Package:
A package is a collection of multiple modules inside a folder.

Example:

math_tools/
    add.py
    multiply.py
