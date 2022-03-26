# Bank Account class
class BankAccount:
    all_accounts = []
    def __init__(self, created_at, int_rate, balance): 
        self.created_at = created_at
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
       self.balance += amount
       return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f" Account was created on {self.created_at} with an interest rate of {self.int_rate * 100}% and the current account balance is ${self.balance *(1+ self.int_rate)}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance *self.int_rate)
        return self

# User class
class User:
    def __init__(self,name,email_address): 
        self.name = name
        self.email_address = email_address
        self.account = {
                        "checking" : BankAccount(created_at = "2021-07-15",int_rate = .04,balance = 1585),
                        "savings" : BankAccount(created_at = "2019-09-18",int_rate = .02,balance = 11000) 
        }
        
    def make_deposit(self,amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account.balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self
    
    def transfer_money(self,user2,amount):
        self.account.balance -= amount
        self.account.balance += amount
        self.display_user_balance()
        user2.display_user_balance()

timmy = User("Timmy Shar","timmyshar@yahoo.com")

timmy.account['checking'].deposit(700).deposit(250).withdraw(100)
timmy.display_user_balance()
