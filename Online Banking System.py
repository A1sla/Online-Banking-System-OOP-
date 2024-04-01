# Object Oriented Programming Project based learning

class Account: #Superclass
    def __init__(self, name, account_number, balance):  # Constructor
        self.name = name # self = reference instances to the class, name = name of the account
        self.account_number = account_number # Account number of the account
        self.balance = balance # Balance of the account

def deposit(self, amount): # Function to deposit money to account
    self.balance += amount # amount is to be added to the account
    print(f"{self.name} Deposited {amount} $. Current Balance is {self.balance}") # Print the result of the final amount

def withdraw(self, amount): # Function to withdraw money
    
    # Create if else statement to check if it is withdrawable or not
    if self.balance >= amount:
        self.balance -= amount
        print(f"{self.name} withdraw {amount} $. Current Balance is {self.balance}")
    else:
        print("You don't have enough money to withdraw")

# Inheritance

class SavingsAccount(Account): #Child class
    def __init__(self, name, account_number, balance, interest_rate): # Constructor for the saving account
        super().__init__(name, account_number, balance) # super() initiates inheritance to the superclass (account)
        self.interest_rate = interest_rate

def add_interest(self): # Function to add interest to the current saving
    interest = self.balance * self.interest_rate # basic formula for interest
    self.deposit(interest) # Adds interest in the deposit method


# Create object for the class to work

account1 = Account("Ryan Reynolds", "12345", 50000) # Instance for the account1 in the account class
account1.deposit(4000) #Call the deposit method
account1.withdraw(10000) #Call the withdraw method
print()

savings_account1 = SavingsAccount("Ryan Reynolds", "12333", 60000, 0.010) # Instance of the savings account in the subclass
savings_account1.deposit(5000)
savings_account1.withdraw(9000)
savings_account1.add_interest()
savings_account1.withdraw(10000)
    
    
        