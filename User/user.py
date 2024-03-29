class User:
    def __init__(self, name, email, balance=0):
        self.name = name
        self.email = email
        self.account_balance = balance

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        self.account_balance += amount
        

    # takes an argument that is the amount of the withdrawl
    def make_withdrawal(self, amount):
        # the specific user's account decreases by the amount of the value received
        self.account_balance -= amount
        

    def display_user_balance(self):
        print(f"Name: {self.name}\nBalance: {self.account_balance}")
        

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)


guido = User("Guido van Rossum", "guido@python.com", 100)
monty = User("Monty Python", "monty@python.com", 50)
joe = User("Joe Bell", "joe@python.com",250)

guido.make_deposit(10)
guido.make_deposit(10)
guido.make_deposit(30)
guido.make_withdrawal(10)
guido.display_user_balance()

monty.make_deposit(10)
monty.make_deposit(10)
monty.make_withdrawal(30)
monty.make_withdrawal(10)
monty.display_user_balance()

joe.make_deposit(50)
joe.make_withdrawal(10)
joe.make_withdrawal(20)
joe.make_withdrawal(10)
joe.display_user_balance()

guido.transfer_money(monty,50)
guido.display_user_balance()
monty.display_user_balance()