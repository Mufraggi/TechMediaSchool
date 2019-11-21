import csv
import sys
import json
from time import sleep
from random import randrange
import plotly.graph_objects as go
from selenium import webdriver
from plotly.subplots import make_subplots
import plotly.express as px




def pront():
    firstPartUrl = "https://finance.yahoo.com/quote/"
    secondPartUrl = "/financials?p="

    driverPath = "./chromedriver"

    print("Can you give compagny?")
    compagny = input()
    driver = webdriver.Chrome(driverPath)
    driver.maximize_window()
    driver.implicitly_wait(1)
    driver = driver
    finalUrl = firstPartUrl + compagny + secondPartUrl + compagny
    driver.get(finalUrl)
    xpathRevenue = ".//div[@class='D(tbr) fi-row Bgc($hoverBgColor):h']"
    print(len(driver.find_elements_by_xpath(xpathRevenue)))
    if (len(driver.find_elements_by_xpath(xpathRevenue)) == 0):
        driver.close()
        return pront()
    return driver.find_elements_by_xpath(xpathRevenue)

element = pront()
for e in element:
    a = e.text.split('\n')
    if ("Total Revenue" in a[0]):
        revenues = a[1]
    elif (len(a) > 1 and "Net Income" in a[0]):
        income = a[1]

list_revenues = revenues.split(' ')
list_incomes = income.split(' ')
i = 0
print (list_revenues)
listToDraw = []
while (i < len(list_revenues)):
    res = float(list_incomes[i].replace(',',"")) / float(list_revenues[i].replace(',',""))
    listToDraw.append(res * 100)
    i = i + 1

secondeValueToPrint = []

y = 0
while (y < len(list_revenues) -1 ):
    secondeValueToPrint.append((float(list_revenues[y + 1].replace(',', "")) / float(list_revenues[y].replace(',', "")))* 100)
    y = y + 1
print(secondeValueToPrint)
year = ["2015","2016", "2017", "2018", "2019"]

fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(x=year, y=listToDraw,
                    mode='lines',
                    name='Percentage of margins profit'),row=1, col=1)
fig.add_trace(go.Scatter(x=year, y=secondeValueToPrint,
                    mode='lines',
                    name='Percentage of Growth rates '),row=1, col=2)
fig.update_layout(height=600, width=800, title_text="Assignement 9")

fig.show()
