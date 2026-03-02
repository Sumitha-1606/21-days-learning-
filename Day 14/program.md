class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def show_marks(self, marks):
        print("Marks:", marks)

class Teacher(Person):
    def show_subject(self, subject):
        print("Subject:", subject
        
s1 = Student("Sumitha", 18)
s1.display()
s1.show_marks(479)

print("-----------")

t1 = Teacher("poorani", 32)
t1.display()
t1.show_subject("science")

output:
Name:Sumitha
Age:18
Marks:479

Name:poorani
Age:32
Subject:Science
