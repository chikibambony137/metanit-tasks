class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def add(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("На балансе недостаточно средств")


user1 = BankAccount(1234567890, 1000)
user1.add(100)
print(user1.balance)
user1.withdraw(50)
print(user1.balance)
user1.withdraw(1550)
print(user1.balance)