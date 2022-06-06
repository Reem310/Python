class User:
    def __init__(self, name, email, balance=0):
        self.name = name
        self.email = email
        self.account_balance = balance

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self

    # takes an argument that is the amount of the withdrawl
    def make_withdrawal(self, amount):
        # the specific user's account decreases by the amount of the value received
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"Name: {self.name}\nBalance: {self.account_balance}")
        return self


guido = User("Guido van Rossum", "guido@python.com", 100)
monty = User("Monty Python", "monty@python.com", 50)
joe = User("Joe Bell", "joe@python.com",250)
guido.make_deposit(10).make_deposit(10).make_deposit(30).make_withdrawal(10).display_user_balance()
monty.make_deposit(10).make_deposit(10).make_withdrawal(30).make_withdrawal(10).display_user_balance()
joe.make_deposit(50).make_withdrawal(10).make_withdrawal(20).make_withdrawal(10).display_user_balance()
