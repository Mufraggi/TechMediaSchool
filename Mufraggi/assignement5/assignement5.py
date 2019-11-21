import numpy as np

def recur(matrice, index):
    if (index == len(matrice[0])):
        return matrice
    i = 0
    while (i < len(matrice[0])):
        res = matrice[index][0] / matrice[i][0]
        matrice[index][i] = res
        i += 1
    return recur(matrice, index+1)

values = [1, 1.22174, 0.75200, 1.10839, 0.67425]
v = np.ones(5)
matrice = np.diag(v,0)
i = 0
while (i < 5):
    matrice[i][0] = values[i]
    i+=1
res = recur(matrice, 0)
print(res)