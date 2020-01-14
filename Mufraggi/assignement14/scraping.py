from selenium import webdriver
from time import sleep
from calls import init_element

def initDriver():
    url = 'http://www.cboe.com/delayedquote/quote-table'
    driverPath = './chromedriver'
    driver = webdriver.Chrome(driverPath)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)
    return driver


def searchButton(driver, str):
    driver.find_element_by_xpath("//div/section/section/input").send_keys(str)
    driver.find_element_by_xpath("//div/section/section/div/input").click()
    sleep(4)
    return driver


def getCalls(driver):
    calls = driver.find_elements_by_xpath('//div/div/table/tbody/tr')
    calls_list = []
    for i in range(len(calls)):
        if i == 4:
            break
        calls_list.append(calls[i].text)
    return init_element(calls_list)


def getMid(driver):
    calls = driver.find_elements_by_xpath('//div/div/div/table/tbody/tr')
    calls_list = []
    for i in range(len(calls)):
        if i == 9:
            break
        if i > 3 and i < 8:
            calls_list.append(calls[i].text.replace('.', ','))
    return calls_list


def getSpot(driver):
    calls = driver.find_elements_by_xpath('//div/div/table/tbody/tr')
    calls_list = []
    for i in range(len(calls)):
        if i == 12:
            break
        if i > 7:
            calls_list.append(calls[i].text)
    return init_element(calls_list)

def getDate(driver):
    dates = driver.find_elements_by_xpath('//div/div/div/h2')
    return dates[2].text

def getLast(driver):
    return driver.find_elements_by_xpath("//div/div/div/div/div/div/div/span/span")[3].text

def isLoaded(driver):
    calls = driver.find_elements_by_xpath('//div/div/table/tbody/tr')
    print(len(calls))
    if len(calls) == 0:
        return False
    return True