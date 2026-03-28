1.count vowel:
s = input("Enter a string: ")
count = 0
for ch in s.lower():
    if ch in 'aeiou':
        count += 1
print("Number of vowels:", count)

output:
Enter a string:
sumitha
Number of vowels:3


2.linear search:
nums = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))
found = False
for i in range(len(nums)):
    if nums[i]== key:
        print("Element found at index", i)
        found = True
        break
if not found:
    print("Element not found")

output:
Enter elements: 10 20 30 40 50
Enter element to search: 50
Element found at index 4
