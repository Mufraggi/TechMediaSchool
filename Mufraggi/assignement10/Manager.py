import csv

from listing import Listing, ElementToList

class result():
    def __init__(self, owner, pair, action, price, id):
        self.id = id
        self.name = owner
        self.pair = pair
        self.action = action
        self.price = price
        self.match = None

class Manager():

    def __init__(self, csv):
        self.listBuyer = Listing()
        self.listSeller = Listing()
        self.listResult = []
        accounts = csv['account']
        pairs = csv["pair"]
        actions = csv['action']
        price = csv["price"]
        for i, val in enumerate(accounts):
            if (self.checkImport(accounts[i],pairs[i], actions[i], price[i]) == False):
                continue
            if ("BUY" in actions[i]):
                self.listBuyer.addNewElement(ElementToList(accounts[i], pairs[i], price[i]))
            elif ("SELL" in actions[i]):
                self.listSeller.addNewElement(ElementToList(accounts[i], pairs[i], price[i]))
            self.listResult.append(result(accounts[i], pairs[i], actions[i], price[i], i))

        self.findTransaction()

    def findTransaction(self):
        for i, buyer in enumerate(self.listBuyer.getListing()):
            for y, seller in enumerate(self.listSeller.getListing()):
                if (buyer.asset == seller.asset and buyer.price > seller.price and buyer.owner != seller.owner):
                    lvlToChangeValueSeller = self.findSellerOrbuyer(seller.owner, "SELL")
                    lvlToChangeValueBuyer = self.findSellerOrbuyer(buyer.owner, 'BUY')
                    if (lvlToChangeValueSeller == -1):
                        print("probléme tout a exploser dans findTransaction")
                        exit(1)
                    self.listResult[lvlToChangeValueSeller].match = lvlToChangeValueBuyer
                    self.listSeller.delElement(y)
                    self.listResult[i].match =  lvlToChangeValueSeller
                    break
        self.lastIteration()

        for e in self.listResult:
            print (e.name,e.pair,e.action,e.price,e.match)

    def findSellerOrbuyer(self, name, action):
        for i, buyer in enumerate(self.listResult):
            if (buyer.name.replace(" ","") == name.replace(" ","") and buyer.action.replace(" ","") == action.replace(" ","")):
                return int(i)
        return -1


    def lastIteration(self):
        tmp = self.listResult
        for i, result in enumerate(self.listResult):
            if (result.match == None):
                self.listResult[i].match = "REJECTED"

    def checkImport(self, name, pair, action, price):
        try:
            price = int(price)
        except:
            return False
        if (type(name) is str and type(pair) is str and type(action) is str and type(price) is int):
            return True
        return False

    def createCsv(self):
        with open('res.csv', 'w') as f:

            firstline = ["id", "account", "pair", "action", "price", 'match']
            writer = csv.writer(f)
            writer.writerow(firstline)
            for result in self.listResult:
                line = [str(result.id), result.name, result.pair, result.action, str(result.price), str(result.match)]
                print(line)
                writer.writerow(line)
            f.close()
