from exportXlsx import createXlsx
from scraping import initDriver, searchButton, getSpot, getMid, getCalls, getDate, getLast, isLoaded


def getChamp():
    print('ici')
    str = input("Can you give me your index?")
    print(str)
    return str


def main():
    champ = getChamp()
    print("icic")
    driver = initDriver()
    driver = searchButton(driver, champ)
    if isLoaded(driver) == False:
        main()
        exit()
    spot = getSpot(driver)
    mid = getMid(driver)
    date = getDate(driver)
    calls = getCalls(driver)
    last = getLast(driver)
    createXlsx(calls, mid, spot, date, last)

main()

