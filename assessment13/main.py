#1 Create a custom math module and import it in another file.
import custom_math

print(custom_math.add(10, 5))  

#2 Create a module to perform string operations.
from string_utils import to_upper, reverse_string

print(to_upper("hello"))
print(reverse_string("python"))

#3 Use random module to generate 5 random integers.
import random

numbers = [random.randint(1, 100) for _ in range(5)]
print(numbers)

#4 Use datetime module to display current date and time.
from datetime import datetime

now = datetime.now()
print("Current Date and Time:", now)

#5 Use math module to find factorial of a number. 
import math

num = 5
print("Factorial:", math.factorial(num))

#6 Create a package shapes with modules for circle and rectangle.
from circle import area as circle_area
from rectangle import area as rectangle_area

print(circle_area(5))
print(rectangle_area(4, 6))


#7  Import multiple functions from one module and use them.
from custom_math import add, subtract

print(add(3, 2))
print(subtract(5, 1))

#8  Write a program to shuffle a list using random module.
import random

items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)

#9  Write a program to calculate the difference between two dates.
from datetime import date

date1 = date(2025, 1, 1)
date2 = date(2025, 1, 15)

difference = date2 - date1
print("Difference in days:", difference.days)

#10  Use os module to list files in a directory.
import os

path = "." 
files = os.listdir(path)

for file in files:
    print(file)
	