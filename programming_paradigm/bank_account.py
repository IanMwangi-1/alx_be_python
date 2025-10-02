class BankAccount:
    def __init__(self, initial_balance=0):
        # store balance as float for arithmetic but format output cleanly
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        # allow numeric strings too
        self.account_balance += float(amount)

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Print balance without unnecessary .0 when it's a whole number
        if self.account_balance.is_integer():
            bal = int(self.account_balance)
        else:
            bal = self.account_balance
        print(f"Current Balance: ${bal}")
