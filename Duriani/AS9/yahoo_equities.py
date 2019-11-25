#!/usr/bin/env python3

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from time import sleep

keywords = ['Total Revenue', 'Net Income']

ticker = input('Please enter a ticker:\n')
driver = webdriver.Chrome()
driver.set_page_load_timeout(2)

try:
    driver.get(f'https://finance.yahoo.com/quote/{ticker}')
except TimeoutException:
    pass


table = None 
try:
    driver.find_element_by_xpath('.//div[@id="quote-summary"]//tbody[@data-reactid="31"]')
    driver.close()
    print(f"The ticker you have entered ({ticker}) does not exists.")
    exit(1)
except NoSuchElementException:
    pass
try:
    driver.find_element_by_xpath('.//li[@data-test="FINANCIALS"]').click()
except TimeoutException:
    pass

sleep(3)

rows = driver.find_elements_by_xpath('.//div[@class="D(tbrg)"]/div[@class="rw-expnded"]')
timeRows = driver.find_elements_by_xpath('.//div[@class="D(tbhg)"]/div/div')[1:]

dico = {'year': [x.find_element_by_xpath('span').text for x in timeRows]}

for row in rows:
    label = row.find_elements_by_xpath('div')[0].find_elements_by_xpath('div')[0].find_elements_by_xpath('div')[0].find_element_by_xpath('span').text
    if label in keywords:
        dataRows = row.find_elements_by_xpath('div')[0].find_elements_by_xpath('div')[1:]
        dico[f'{label}'] = []
        for data in dataRows:
            dico[f'{label}'].append(int(data.find_element_by_xpath('span').text.replace(',', '')))
            
driver.close()
sleep(2)

dico['Net Income'].reverse()
dico['Net Income'].pop()
dico['Total Revenue'].reverse()
dico['Total Revenue'].pop()
dico['year'].reverse()
dico['year'].pop()

dico['growthRate'] = [((dico['Total Revenue'][i+1] - x) / x) * 100 for (i, x) in enumerate(dico['Total Revenue'][:-1])]
dico['profit margin'] = [(x/y) * 100 for (x, y) in zip(dico['Net Income'], dico['Total Revenue'])]

fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Scatter(
    x=dico['year'],
    y=dico['growthRate'],
    name='Revenue Growth'),
    row=1, col=1)

fig.add_trace(go.Scatter(
    x=dico['year'],
    y=dico['profit margin'],
    name='Profit Margin'),
    row=1, col=2)

fig.update_layout(
    title=f'Revenue growth & Profit margin for {ticker}',
    xaxis_title='Year',
    yaxis_title='Value (%)')

fig.show()