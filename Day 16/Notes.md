Encapsulation:
Encapsulation is another core concept in Object-Oriented Programming (OOP).
Encapsulation means hiding internal data and controlling access to it.
It protects object data from direct modification.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    def show_marks(self):
        print("Marks:", self.__marks)

s1 = Student("Sumitha", 95)

s1.show_marks()
Output:
Marks: 95
Here __marks cannot be accessed directly outside the class.

Access Using Methods:

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount(1500)

acc.deposit(500)
acc.show_balance()

Output:

Balance: 2000
