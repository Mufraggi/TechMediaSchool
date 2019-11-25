import numpy as np

class KeyPaire():
    def __init__(self, keyPaire, value):
        self.keypaire = keyPaire
        self.value = value

def getKeyPair(listKeyPaire, nbKeyPair):
    if (len(listKeyPaire) == nbKeyPair):
        return listKeyPaire
    print("Can you give me your currencie ?")
    currencie = input()
    print("Can you give me the price ?")
    price = float(input())
    if (len(listKeyPaire) == 0):
        listKeyPaire.append(KeyPaire(currencie, 1))
    else:
        listKeyPaire.append(KeyPaire(currencie, price))
    return getKeyPair(listKeyPaire, nbKeyPair)


def recur(matrice, index):
    if (index == len(matrice[0])):
        return matrice
    i = 0
    while (i < len(matrice[0])):
        res = matrice[index][0] / matrice[i][0]
        matrice[index][i] = res
        i += 1
    return recur(matrice, index+1)

def start():
    print("how meny you whant to set a currency")
    nbCurrency = int(input())
    return getKeyPair([], nbCurrency), nbCurrency

list, nbCurrency = start()
values = []
for element in list:
    values.append(element.value)
v = np.ones(nbCurrency)
matrice = np.diag(v, 0)
i = 0
while (i < nbCurrency):
    matrice[i][0] = values[i]
    i+=1
res = recur(matrice, 0)
print(res)