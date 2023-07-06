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
