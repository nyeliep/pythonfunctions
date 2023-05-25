# 1) Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these methods to the Student class
            #  - show_full_name
            #  - year_of_birth
            #  - show_initials
class Student:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
    
    def show_full_name(self):
        return self.first_name + " " + self.last_name
    
    def year_of_birth(self):
        current_year = 2023
        return current_year - self.age
    
    def show_initials(self):
        return self.first_name[0].upper() + "." + self.last_name[0].upper() + "."

# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and three methods (behaviours) for each class and implement them

# Then do the following in the interpreter 
# Create two instances of each class. 
# Call each of the methods you defined.
class Car:
    manufacturer = "Jeep"
    
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    def honk(self):
        return "Beep beep!"
    
    def info(self):
        return f"This is a {self.color} {self.year} {self.manufacturer} {self.model}."


class Fruit:
    type = "Apple"
    
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste
    
    def is_edible(self):
        return True
    
    def info(self):
        return f"This is a {self.color} {self.name} with {self.taste} flavor."


class Account:
    bank_name = "Equity"
    
    def __init__(self, owner_name, balance, account_number):
        self.owner_name = owner_name
        self.balance = balance
        self.account_number = account_number
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. Balance is now {self.balance}."
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrew {amount}. Balance is now {self.balance}."
        
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.deposits.append(amount)

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.withdrawals.append(amount)
        else:
            print("Insufficient balance!")

    def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10:
            total_deposits = sum(self.deposits)
            if amount <= total_deposits / 3:
                self.loan_balance += amount
                print("Loan borrowed successfully!")
            else:
                print("Loan amount exceeds the limit.")
        else:
            print("Loan request not eligible.")

    def repay_loan(self, amount):
        if self.loan_balance > 0:
            if amount > self.loan_balance:
                self.balance += amount - self.loan_balance
                self.loan_balance = 0
                print("Loan fully repaid. Excess amount added to the account balance.")
            else:
                self.loan_balance -= amount
                print("Loan partially repaid.")
        else:
            print("No outstanding loan to repay.")

    def transfer(self, amount, recipient_account):
        if amount <= self.balance:
            self.balance -= amount
            recipient_account.deposit(amount)
            print("Transfer successful.")
        else:
            print("Insufficient balance for transfer.")

            


account = BankAccount("Nyeliep Giel")
account.deposit(1500)
account.withdrawal(500)
account.borrow_loan(1000)
account.repay_loan(700)
balance = account.check_balance()
recipient_account = BankAccount("Mary")
account.transfer(300, recipient_account)
print(account.check_balance())
print( recipient_account.check_balance())
