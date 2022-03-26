class User:
    def __init__(self,name,email_address): 
        self.name = name
        self.email_address = email_address
        self.account_balance = 0 
        
    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"{self.name},Balance: ${self.account_balance}")
    
    def transfer_money(self,user2,amount):
        self.account_balance -= amount
        user2.account_balance += amount
        self.display_user_balance()
        user2.display_user_balance()

timmy = User("Timmy Shar","timmyshar@yahoo.com")
tony = User("Tony Shar","Tonyshar5@rocketmail.com")
olga = User("Olga Olevksy", "oolevsky@mednet.ucla.edu")
# print(timmy.email_address)


timmy.make_deposit(700)
olga.make_deposit(1000)
timmy.make_deposit(250)
timmy.make_withdrawal(100)
tony.make_deposit(1500)
olga.make_withdrawal(200)
tony.make_deposit(325)
olga.make_withdrawal(150)
tony.make_withdrawal(200)

timmy.transfer_money(olga,100)


timmy.display_user_balance()
tony.display_user_balance()
olga.display_user_balance()



#Chaining
timmy.make_deposit(700).make_deposit(250).make_withdrawal(100).display_user_balance()




