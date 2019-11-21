
def checkInput(input):
    imputsTrue = ["1", "2", "3", "4", "5", "6", "7"]
    bool = False
    for imputTrue in imputsTrue:
        if(imputTrue in input):
            bool = True
    return bool == True

def printPront():
    prontText = "****************************************\n** Welcome to simply trade v, 1 **\n****************************************\nMarket Value of Securities $0\nCash Balance $0\nWould you like to:"
    print(prontText)

def pront():
    printPront()
    newInput = input()
    if (checkInput(newInput) == False):
        print('****************************')
        print("Your input is wrong")
        print('****************************')
        return pront()

    if (newInput == '7'):
        return
    return pront()

pront()