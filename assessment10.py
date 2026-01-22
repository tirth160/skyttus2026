#1 Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake. 
class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, value):
        self.speed += value
        print(f"Accelerated! Current speed: {self.speed} km/h")

    def brake(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0
        print(f"Braked! Current speed: {self.speed} km/h")


my_car = Car("Toyota", "Corolla")
my_car.accelerate(50)
my_car.brake(20)
class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, value):
        self.speed += value
        print(f"Accelerated! Current speed: {self.speed} km/h")

    def brake(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0
        print(f"Braked! Current speed: {self.speed} km/h")

# Example
my_car = Car("Toyota", "Corolla")
my_car.accelerate(50)
my_car.brake(20)

#2 Create a BankAccount class with deposit and withdraw methods.
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Balance: {self.balance}")
        else:
            print("Insufficient balance!")

# Example
account = BankAccount("Alice")
account.deposit(500)
account.withdraw(200)

#3  Create a Student class with a method to calculate average marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of marks

    def average(self):
        avg = sum(self.marks) / len(self.marks)
        print(f"{self.name}'s average marks: {avg}")

# Example
student = Student("Bob", [80, 90, 70])
student.average()

#4  Create a Rectangle class with methods to find area and perimeter. 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area: {self.length * self.width}")

    def perimeter(self):
        print(f"Perimeter: {2 * (self.length + self.width)}")

# Example
rect = Rectangle(5, 3)
rect.area()
rect.perimeter()

# 5 Create an Employee class that displays salary details.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print(f"{self.name}'s salary: {self.salary}")

# Example
emp = Employee("John", 50000)
emp.display_salary()

#6  Create a Book class to store title, author, and price, and display details.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

# Example
book = Book("Python 101", "Alice", 300)
book.display_details()
 
#7  Create a Circle class to find area and circumference.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area: {math.pi * self.radius ** 2:.2f}")

    def circumference(self):
        print(f"Circumference: {2 * math.pi * self.radius:.2f}")

# Example
c = Circle(5)
c.area()
c.circumference()
 
#8 Create a Laptop class with a method to apply discounts on price.
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, discount):
        self.price -= self.price * (discount / 100)
        print(f"Price after {discount}% discount: {self.price}")

# Example
laptop = Laptop("Dell", 50000)
laptop.apply_discount(10)

#9 Create a Flight class with seat booking functionality.
class Flight:
    def __init__(self, flight_number, seats):
        self.flight_number = flight_number
        self.seats = seats
        self.booked = 0

    def book_seat(self):
        if self.booked < self.seats:
            self.booked += 1
            print(f"Seat booked! {self.seats - self.booked} seats left.")
        else:
            print("No seats available!")

# Example
f = Flight("AI101", 3)
f.book_seat()
f.book_seat()
f.book_seat()
f.book_seat()

#10  Create a Shop class with a method to add and list products.
class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product} added to {self.name}")

    def list_products(self):
        print(f"Products in {self.name}:")
        for product in self.products:
            print("-", product)

# Example
shop = Shop("MyShop")
shop.add_product("Laptop")
shop.add_product("Phone")
shop.list_products()
	