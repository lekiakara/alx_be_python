# bank_account.py

class BankAccount:
    """A simple bank account class with basic operations."""

    def __init__(self, initial_balance=0.00):
        """Initialize account with an optional starting balance (default = 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance}")
