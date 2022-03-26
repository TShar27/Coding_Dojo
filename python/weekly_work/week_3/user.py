class User:
    def __init__(self,name,email_address): 
        self.name = name
        self.email_address = email_address
        self.account_balance = 0 
        
    def make_deposit(self,amount):
        self.account_balance += amount

    def make_withdrawal(self,amount):
        self.account_balance -= amount 
    
    def display_user_balance(self):
        print(self.name,f"(balance {self.account_balance}")

timmy = User("Timmy Shar","timmyshar@yahoo.com")
# print(timmy.email_address)


timmy.make_deposit(100)
timmy.make_withdrawal(200)
print(timmy.account_balance)




