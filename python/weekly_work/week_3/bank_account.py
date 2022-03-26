# from msilib.schema import SelfReg


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

# timmy.deposit(100).display_account_info()

    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()


checking = BankAccount("2015-05-19",.02,3000)
savings = BankAccount("1993-09-22",.075,12000)

checking.deposit(1450).deposit(800).deposit(400).withdraw(650).yield_interest()
savings.deposit(1000).deposit(2500).deposit(430).withdraw(750).yield_interest()

BankAccount.print_all_accounts()


