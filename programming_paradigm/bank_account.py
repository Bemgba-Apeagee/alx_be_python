class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize a bank account with an optional starting balance."""
        self.current_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.current_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount > self.current_balance:
            return False
        else:
            self.current_balance -= amount
            return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.current_balance:.2f}")
