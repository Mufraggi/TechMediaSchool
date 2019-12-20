from time import sleep

import pandas as pd
import requests
import io
import plotly.graph_objects as go


def checkCodeProduct(bool):
    if (bool == True):
        print("Your product code doesn't exist")
    print("Can you try one product code?")
    codeProduct = str(input())

    if (len(codeProduct) != 13):
        print("Your product code need 13 numbers")
        checkCodeProduct(True)
    else:
        return createXlsx(codeProduct)


def createXlsx(name):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'request_action': 'get_data',
        'reformat': 'true',
        'from_results_page': 'true',
        'years_option': 'specific_years',
        'delimiter': 'comma',
        'output_type': 'multi',
        'periods_option': 'all_periods',
        'output_view': 'data',
        'to_year': '2019',
        'from_year': '2009',
        'output_format': 'excelTable',
        'original_output_type': 'default',
        'annualAveragesRequested': 'false',
        'series_id': name
    }
    response = requests.post('https://data.bls.gov/pdq/SurveyOutputServlet', headers=headers, data=data)
    c = io.BytesIO(response.content)
    try:
        df = pd.read_excel(c, skiprows=9)
        return df
    except:
        return checkCodeProduct(True)

def formatData(df):
    finalMount = []
    for index, row in df.iterrows():
        for mount in mounts:
            finalMount.append(str(row["Year"]) + '_' + mount)

    df = df.drop('Year', axis=1)
    listValue = []
    for index, row in df.iterrows():
        for cel in row:
            if ("nan" not in str(cel)):
                listValue.append(cel)
    return finalMount, listValue


mounts = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print("Can you try one other product code?")
name = str(input())
df = createXlsx(name)
finalMount, listValue = formatData(df)

fig = go.Figure()
fig.add_trace(go.Scatter(
                x=finalMount,
                y=listValue,
                line_color='deepskyblue',
                opacity=0.8))
fig.show()

