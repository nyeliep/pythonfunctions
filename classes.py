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
