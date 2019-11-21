#!/usr/bin/env python
import csv
import sys
import json
from time import sleep
from random import randrange

from selenium import webdriver

class res():
    def __init__(self, nameCountry, value):
        self.nameContry = nameCountry
        self.value = value


    def __str__(self):
        return {
            "contry": self.nameContry,
            "value": self.value,
        }





with open("tests/test.json") as json_file:
    data = json.load(json_file)
urlBase = data['baseUrlAll']
baseUrlOther = data['baseUrlOther']
driverPath = data['driverPath']
endUrl = data['endOffBaseUrlOther']
iso = data['iso']

urlBase = []
if ( 'all' in sys.argv[1] ):
    y = 0
    while (y != 5):
        urlBase.append(data['baseUrlOther'] + iso[randrange(len(iso))] + data["endOffBaseUrlOther"])
        y += 1
elif (len(sys.argv[1]) > 0):
    urlBase.append(data['baseUrlOther'] + sys.argv[1] + data["endOffBaseUrlOther"])
else:
    print("Error: vive séélénium")
    exit(1)



driver = webdriver.Chrome(driverPath)
driver.maximize_window()
driver.implicitly_wait(5)
driver = driver
for url in urlBase:

    driver.get(url)
    sleep(5)
    listElement = driver.find_element_by_id("contenttablejqx-PartnerGrid")
    _list = listElement.find_elements_by_xpath(".//div[@role='row']")
    i = 1
    listResult = []
    while (i != 5):
        el = _list[i].find_elements_by_xpath('.//div')
        listResult.append(res(el[0].text, el[2].text))
        i+=1
    if (len(sys.argv) == 3 and 'save'in sys.argv[2]):
        print('ici')
        with open('employee_file.csv', mode='w') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for e in listResult:
                employee_writer.writerow([e.nameContry, e.value])
    else:
        for e in listResult:
            print(e.nameContry + ' ' + e.value)




