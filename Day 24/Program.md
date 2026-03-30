1.Find factor :
num = int(input("Enter a number: "))
print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

Output:
Enter a number:6
Factors are 1 2 3 6

2.Find GCD :
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    a, b = b, a % b
print("GCD =", a)

Output:
Enter first number: 15
Enter second number: 25
GCD = 5
