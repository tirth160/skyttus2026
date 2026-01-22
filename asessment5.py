# 1. Print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

# 2. Display multiplication table for a given number.
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 3. Find factorial of a number.
n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)

# 4. Generate the first N Fibonacci numbers. 
n = 10
a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b

# 5. Check if a number is prime. 
num = 7
flag = 0

for i in range(2, num):
    if num % i == 0:
        flag = 1

if flag == 0:
    print("Prime")
else:
    print("Not Prime")

# 6. Reverse a number (e.g., 123 → 321).
num = 123
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

print(rev)

# 7. Count digits in a number. 
num = 4567
count = 0

while num > 0:
    count += 1
    num = num // 10

print(count)

# 8. Find sum of even numbers between 1–100.
sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum += i

print(sum)


 
# 9. Print a pyramid pattern.
n = 5

for i in range(1, n + 1):
    print("*" * i)

# 10.Find all divisors of a number.
num = 12

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
	
# 1. Check if a person is eligible to vote (age ≥ 18). 
age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 2. Grade calculator based on marks: 90+ = A, 80+ = B, else C.
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")
 
# 3. Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go. 
light = "Red"

if light == "Red":
    print("Stop")
elif light == "Yellow":
    print("Wait")
else:
    print("Go")

# 4.ATM withdrawal check: sufficient balance or not. 
balance = 5000
withdraw = 2000

if withdraw <= balance:
    print("Withdraw successful")
else:
    print("Insufficient balance")

# 5.Check if a number is positive, negative, or zero.
num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 6. Check if a number lies within a given range.
num = 15

if num >= 10 and num <= 20:
    print("Number is in range")
else:
    print("Number is not in range")

# 7. Username & password verification. 
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")

# 8.Electricity bill calculator based on units consumed.
units = 120

if units <= 50:
    bill = units * 2
elif units <= 100:
    bill = units * 3
else:
    bill = units * 5

print("Electricity bill =", bill)

# 9. Simple calculator (add, subtract, multiply, divide).
a = 10
b = 5
op = "+"

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
else:
    print(a / b)

# 10. Check type of triangle (equilateral, isosceles, scalene).
a = 5
b = 5
c = 5

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
	