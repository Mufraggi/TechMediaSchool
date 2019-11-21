import csv
import io

import pandas as pd
import requests





def test():
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
        'series_id': 'APU0000702212'
    }

    try:
        response = requests.post('https://data.bls.gov/pdq/SurveyOutputServlet', headers=headers, data=data)
    except:
        return False
    with open('at2.xlsx', 'wb') as f:
        f.write(response.content)
    df = pd.read_excel('at2.xlsx', skiprows=9)

    print(df)
    return df

test()
#with open('at2.xlsx', 'wb') as f:
 #   f.write(response.content)
#print(response.content)


#url = 'https://download.bls.gov/pub/time.series/ap/ap.data.0.Current'
#mounts = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

#r = requests.get(url)
#if r.ok:
    data = r.content.decode('utf8')

    df = pd.read_csv(io.StringIO(data), sep='\t')
    df = df.drop_duplicates("series_id        ")
    for col in df.columns:
        print('|', col, '|')
    print(df)
