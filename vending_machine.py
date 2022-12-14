import zope as zope


class VendingMachine(zope.interface.Interface):
    all_drinks = zope.interface.Attribute

    def get_product(self, name, price, volume):
        return name, price, volume
