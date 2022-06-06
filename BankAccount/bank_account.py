class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0):
        self.int_rate=int_rate
        self.balance=balance

    # your code here! (remember, this is where we specify the attributes for our class)
    # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
    # your code here
        self.balance -= amount
        return self

    def display_account_info(self):
    # your code here
        print(f"Balance: {self.balance}")

    def yield_interest(self):
    # your code here
        if self.balance>=0:
            self.balance=self.int_rate*self.balance
            return self

user1=BankAccount(10,-1)
user2=BankAccount(5,100)
user1.withdraw(20)
user1.deposit(20)
user1.yield_interest()
user1.display_account_info()