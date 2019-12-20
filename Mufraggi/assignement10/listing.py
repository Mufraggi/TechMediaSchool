
class ElementToList():
    def __init__(self, owner, asset, price):
        self.owner = owner
        self.asset = asset
        self.price = price




class Listing():
    def __init__(self):
        self.Listing = []

    def getListing(self):
        return self.Listing

    def addNewElement(self, element):
        self.Listing.append(element)

    def delElement(self, i):
        self.Listing.pop(int(i))


