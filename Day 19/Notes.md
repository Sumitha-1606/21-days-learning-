Searching:
Searching means finding a specific element in a list or array.

types:
Linear Search,Binary Search

Linear Search
Linear search checks each element one by one.

Program

numbers = [10, 20, 30, 40, 50]

key = int(input("Enter number to search: "))

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element found at position", i)
        break
else:
    print("Element not found")

Example Output

Enter number to search: 30
Element found at position 3

Time Complexity

O(n)

Binary Search
Binary search works only on sorted lists.
It divides the list into halves.

Program

numbers = [10, 20, 30, 40, 50]

key = int(input("Enter number to search: "))

low = 0
high = len(numbers) - 1

while low <= high:
    if numbers[mid] == key:
        print("Element found at index", mid)
        break
    elif numbers[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")

Example Output

Enter number to search: 40
Element found at index 3
