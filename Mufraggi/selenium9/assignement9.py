
import plotly.graph_objects as go
from selenium import webdriver
from plotly.subplots import make_subplots

def pront():
    firstPartUrl = "https://finance.yahoo.com/quote/"
    secondPartUrl = "/financials?p="

    driverPath = "./chromedriver"

    print("Can you give compagny?")
    compagny = str(input())
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
list_incomes.reverse()
list_revenues.reverse()
print(list_revenues)
i = 0
print (list_revenues)
listToDraw = []
while (i < len(list_revenues)):
    res = float(list_incomes[i].replace(',',"")) / float(list_revenues[i].replace(',',""))
    listToDraw.append(res * 100)
    i = i + 1

growth_rates = []

y = 1
print(list_revenues)
while (y < len(list_revenues) -1 ):
    print(list_revenues[y].replace(',',""))
    print(list_revenues[y - 1].replace(',',""))
    growth_rates.append(((float(list_revenues[y].replace(',', "")) - (float(list_revenues[y - 1].replace(',', "")))) / float(list_revenues[y].replace(',', ""))) * 100)
    y = y + 1
#exit(0)

print(growth_rates)
year = ["2015","2016", "2017", "2018", "2019"]
year2 = ["2016", "2017", "2018", "2019"]

fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(x=year, y=listToDraw,
                    mode='lines',
                    name='Percentage of margins profit'),row=1, col=1)
fig.add_trace(go.Scatter(x=year2, y=growth_rates,
                    mode='lines',
                    name='Percentage of Growth rates '),row=1, col=2)
fig.update_layout(height=600, width=800, title_text="Assignement 9")

fig.show()
