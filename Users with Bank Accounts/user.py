from Bank_Account import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        self.account += amount
        

    # takes an argument that is the amount of the withdrawl
    def make_withdrawal(self, amount):
        # the specific user's account decreases by the amount of the value received
        self.account -= amount
        

    def display_user_balance(self):
        print(f"Name: {self.name}\nBalance: {self.account.balance}")
        

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
joe = User("Joe Bell", "joe@python.com")

guido.account.deposit(50).deposit(50).deposit(100).withdraw(20).yield_interest().display_account_info()
guido.display_user_balance()