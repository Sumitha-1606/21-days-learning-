Recursion:
Recursion is when a function calls itself to solve a problem.
Instead of using loops, the function repeatedly calls itself until a stopping condition is reached.

Structure
def function_name():
    if condition:      
        return value
    else:
        return function_name()

Two important parts:
Base case → stops recursion
Recursive call → function calls itself

Example: Factorial Using Recursion

def factorial(n):
    if n == 1:          
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter number: "))
print("Factorial:", factorial(num))

Output Example
Enter number: 5
Factorial: 120

5 × 4 × 3 × 2 × 1 = 120

Example: Sum of Numbers

def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n-1)

print(sum_numbers(5))

Output:

15

Example: Fibonacci Series

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

Output:
8
