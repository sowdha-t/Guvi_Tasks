"""Create a Base class BankAccount with attributes like account_number and
balance and methods like deposit and withdraw. Inherit from this class to create
subclasses SavingsAccount and CurrentAccount. The savings account should have an interest rate
and a method to calculate interest rate. The current account should have a minimum
balance requirement. Implement encapsulation to protect the account balance and ensure that withdrawals
cannot exceed the balance or minimum balance requirements"""

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance                #Encapsulation of Account Balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    interest_rate = 0.04
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = SavingsAccount.interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Interest for the Savings Account Balance: {interest}")
        self.deposit(interest)


class CurrentAccount(BankAccount):
    minimum_balance = 500
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.minimum_balance = CurrentAccount.minimum_balance

    def withdraw(self, amount):
        if amount > 0 and ( self.get_balance() - amount) >= self.minimum_balance:
            super().withdraw(amount)
        else:
            print(f"Withdrawal denied. Balance cannot go below minimum requirement value of {CurrentAccount.minimum_balance}.")

print("Savings Account Execution")
savings = SavingsAccount("SA123", 1000)
savings.deposit(500)
savings.calculate_interest()
savings.withdraw(200)
print("Current Account Execution")
# Current Account
current = CurrentAccount("CA456", 2000)
current.withdraw(800)   # Allowed
current.withdraw(1500)  # Denied (would go below min balance)




