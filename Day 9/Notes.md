Dictionaries in Python:
A dictionary is a collection of key-value pairs.
Each value is accessed using its key.
Dictionaries are unordered, changeable, and do not allow duplicate keys.
syntax:
dict_name = {
    "key1": value1,
    "key2": value2
}

Example:
student = {
    "name": "Sumitha",
    "age": 18,
    "dept": "ECE"
}

print(student)
Output:
{'name': 'Sumitha', 'age': 18, 'dept': 'ECE'}

Access value:
print(student["name"])
print(student["age"])
Output:
Sumitha
18

Add new key
student["city"] = "Chennai"
print(student)

Update key
student["age"] = 21

Remove key
student.pop("dept")

Loop through dictionary
for key, value in student.items():
    print(key, value)
