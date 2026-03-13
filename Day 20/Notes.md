Sorting Algorithms
Sorting means arranging elements in ascending or descending order.

1.Using Built-in Sort
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)

Output
[1, 2, 5, 8, 9]

2.Bubble Sort
Bubble sort repeatedly swaps adjacent elements if they are in the wrong order.

Program:
numbers = [5, 2, 8, 1, 9]
n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print("Sorted list:", numbers)

Output
Sorted list: [1, 2, 5, 8, 9]

3.Sorting in Descending Order
numbers = [5, 2, 8, 1, 9]
numbers.sort(reverse=True)
print(numbers)

Output:
[9, 8, 5, 2, 1]

