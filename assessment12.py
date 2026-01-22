# 1. To-Do List CLI 
todo_list = []

while True:
    print("\n1. Add Task\n2. Show Tasks\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        todo_list.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(todo_list, 1):
            print(f"{i}. {t}")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

# 2. Bank Management System 
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
            print(f"Withdrew {amount}. Balance: {self.balance}")
        else:
            print("Insufficient balance")

# Test
account = BankAccount("Alice", 1000)
account.deposit(500)  # 1500
account.withdraw(300) # 1200
account.withdraw(2000) # Insufficient balance

