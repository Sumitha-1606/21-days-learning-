1.Ask user age 
age = input("Enter your age: ")
print("Your age is", age)
Output:
Enter your age: 18
Your age is 18
2. Add two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)
Output
Enter first number: 16
Enter second number: 4
Sum = 20
3.Ask name and print welcome message
name = input("Enter your name: ")
print("Welcome", name)
Output:
Enter your name: Sumitha
Welcome Sumitha
4. Multiply two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Product =", a * b)
Output:
Enter first number: 5
Enter second number: 7
Product = 35

if statement:
1.Check if number is Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
Output
Enter a number: 10
Even number
2.Check if person is eligible to vote
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
Output
Enter your age: 22
Eligible to vote
3.Find largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest number is", a)
else:
    print("Largest number is", b)
Output
Enter first number: 25
Enter second number: 10
Largest number is 25
4.Grade calculator
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
output:
    Enter your marks: 80
    Grade B
