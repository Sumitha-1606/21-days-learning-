List sorting program:
numbers = []
n = int(input("How many numbers? "))
for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)
numbers.sort()
print("Sorted List:", numbers)

output:
How many numbers? 4
Enter number: 10
Enter number: 5
Enter number: 16
Enter number: 15

Sorted List: [5, 10, 15, 16,]
