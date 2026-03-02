Inheritance:
  Inheritance allows one class to inherit properties and methods from another class.

It promotes:
  Code reuse
  Cleaner structure

🔹 Basic Concept
Parent Class → Base class
Child Class → Derived class
example:
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle started")

class Car(Vehicle):  
    def display(self):
        print("Brand:", self.brand)

car1 = Car("Toyota")
car1.start()
car1.display()

output:
Vehicle started
Brand: Toyota

