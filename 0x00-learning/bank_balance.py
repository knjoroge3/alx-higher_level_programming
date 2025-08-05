#!/usr/bin/python3

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("{} has deposited {} and this is his balance {}".format(self.owner, amount, self.balance))

    def withdraw(self, amount):

        if amount > self.balance:
            print("{} has insufficient funds".format(self.owner))
        else:
            self.balance -= amount
            print("{} has withdrwan {} and there new balance is {}".format(self.owner, amount, self.balance))

owner1 = BankAccount("Kennedy", 50)
owner2 = BankAccount("Talam")

owner1.deposit(2000)
owner2.deposit(5000)
owner1.withdraw(5000)
owner2.withdraw(3000)
