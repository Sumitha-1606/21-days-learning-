1.palindrome:
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

output:
Enter a word:Madam
palindrome
Enter a word:Hello
Not palindrome

2.password strength:
password = input("Enter password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")

output:
Enter password:abcd@1234
strong password
