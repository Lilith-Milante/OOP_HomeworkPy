import zope as zope

from OOP_Homework_Py.vending_machine import VendingMachine

class HotDrinksVendingMachine():

    zope.interface.implements(VendingMachine)

    def __init__(self):
        self.all_drinks = []

    def HotDrinksVendingMachine(self, allDrinks):


    def get_product(self, name, volume, temperature, all_drinks):
        for i in range(all_drinks):
