1.Car Speed System
class Car:
    def __init__(self):
        self.__speed = 0 
    def set_speed(self, speed):
        self.__speed = speed
    def show_speed(self):
        print("Car Speed:", self.__speed)

c = Car()
c.set_speed(60)
c.show_speed()

output:
Car Speed: 60

2.class Mobile:
    def __init__(self):
        self.__battery = 60
    def charge(self, amount):
        self.__battery += amount
        print("Battery charged")
    def show_battery(self):
        print("Battery Level:", self.__battery)

m = Mobile()
m.charge(11)
m.show_battery()

output:
Battery charged
Battery Level:71

