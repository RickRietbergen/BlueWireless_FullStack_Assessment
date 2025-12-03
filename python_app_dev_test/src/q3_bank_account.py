#fill in your answers here
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance=0):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def get_balance(self):
        return None

if __name__ == "__main__":
    acc = BankAccount(100)
    acc.deposit(50)
    print(acc.get_balance())
    acc.withdraw(120)
    print(acc.get_balance())
