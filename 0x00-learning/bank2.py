#!/usr/bin/python3

""" this is a program that tries to determine when you will
become a millinioare with the current situation"""

class Millionaire:

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def current_amount(self, amount):
        amount = None
        deficit = None
        monthly_income = int(input("how much money do you earn per month? "))
        months = None

        try:
            amount = int(input("How much money do you have in your account? "))

            if amount < 100000:
                deficit = 1000000 - amount

                months = (deficit / monthly_income)
            else:
                print("You already are a millionaire")

        except ValueError:
            print("Amount can only be in figures")

        finally:
            print("If you have only {} then to be a millionaire you have a deficit of {} and you will need to work for {} month(s) to achive your goal. All the best".format(amount, deficit, months))


