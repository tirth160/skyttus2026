#1 Create a base class Animal and subclasses Dog and Cat.
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Test
dog = Dog()
cat = Cat()
dog.speak()  # Woof!
cat.speak()  # Meow!

#2 Create a class hierarchy for Vehicle → Car → ElectricCar. 
class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def info(self):
        print("This is a car")

class ElectricCar(Car):
    def info(self):
        print("This is an electric car")

# Test
ecar = ElectricCar()
ecar.info()  # This is an electric car

#3 Implement method overriding in a base and derived class.
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

# Test
c = Child()
c.greet()  # Hello from Child

#4  Demonstrate multiple inheritance with two parent classes. 
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

# Test
child = Child()
child.skills()  # Gardening (Father comes first)

#5  Create a polymorphic function that works with different shapes. 
class Circle:
    def area(self, r):
        return 3.14 * r * r

class Square:
    def area(self, a):
        return a * a

def print_area(shape, value):
    print("Area:", shape.area(value))

# Test
c = Circle()
s = Square()
print_area(c, 5)  # Area: 78.5
print_area(s, 4)  # Area: 16

#6  Create a Bank system with SavingsAccount and CurrentAccount classes. 
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def show_balance(self):
        print("Balance:", self.balance)

class SavingsAccount(BankAccount):
    def add_interest(self):
        self.balance += self.balance * 0.05

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount

# Test
s = SavingsAccount(1000)
s.add_interest()
s.show_balance()  # 1050.0

c = CurrentAccount(2000)
c.withdraw(500)
c.show_balance()  # 1500

#7  Create a class with private attributes and getter/setter methods.
class Person:
    def __init__(self, name):
        self.__name = name  # private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

# Test
p = Person("Alice")
print(p.get_name())  # Alice
p.set_name("Bob")
print(p.get_name())  # Bob

#8   Create a Teacher and Student class to show inheritance.
class Teacher:
    def teach(self):
        print("Teaching...")

class Student(Teacher):
    def study(self):
        print("Studying...")

# Test
s = Student()
s.teach()   # Teaching...
s.study()   # Studying...
class Teacher:
    def teach(self):
        print("Teaching...")

class Student(Teacher):
    def study(self):
        print("Studying...")

# Test
s = Student()
s.teach()   # Teaching...
s.study()   # Studying...

#9    Create a MusicPlayer class and subclass Spotify to override play method. 
class MusicPlayer:
    def play(self):
        print("Playing music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")

# Test
m = MusicPlayer()
s = Spotify()
m.play()  # Playing music
s.play()  # Playing music on Spotify

#10 Demonstrate the use of super() in inheritance.	
class Parent:
    def __init__(self):
        print("Parent init")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call parent constructor
        print("Child init")

# Test
c = Child()
# Output:
# Parent init
# Child init
