#fill in your answers here
class InsufficientFundsError(Exception):
    """Raised when attempting to withdraw more than the available balance."""
    pass

class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += float(amount)
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise InsufficientFundsError(f"Insufficient funds: attempted to withdraw {amount} but balance is {self._balance}")
        self._balance -= float(amount)
        return self._balance

    def get_balance(self):
        return self._balance

if __name__ == "__main__":
    acc = BankAccount(100)
    acc.deposit(50)
    print(acc.get_balance())   # 150.0
    acc.withdraw(120)
    print(acc.get_balance())   # 30.0
