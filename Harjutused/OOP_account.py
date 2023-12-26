"""
Lisa meetod tranfer mis saadab raha ühelt kontolt teisele (kasuta olemasolevaid meetodeid). Meetod peab kontrollima:

kas sellised kontod on pangas olemas
kas lähtekontolt on võimalik selline hulk raha välja võtta
Kui tehing õnnestub, tagastab meetod True, vastasel juhul False
"""


class Account:
    def __init__(self, account_number: str, balance: int = 0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: Account) -> None:
        self.accounts[account.account_number] = account

    def transfer(self, from_acc_num: str, to_acc_num: str, amount: int) -> bool:
        if from_acc_num in self.accounts and to_acc_num in self.accounts:
            if self.accounts[from_acc_num].withdraw(amount):
                self.accounts[to_acc_num].deposit(amount)
                return True
        return False


bank = Bank()
acc1 = Account("123", 500)
acc2 = Account("456", 200)
bank.add_account(acc1)
bank.add_account(acc2)
print(False == bank.transfer("1231", "456", 100))
print(False == bank.transfer("123", "4561", 100))