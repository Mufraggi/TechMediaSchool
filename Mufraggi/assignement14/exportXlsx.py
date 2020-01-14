import pandas as pd
import xlsxwriter

def createXlsx(calls, mid, spot, date, last):
    dfCall = pd.DataFrame({"Calls"})
    dfSpot = pd.DataFrame({"Spot"})
    dfDate = pd.DataFrame({str((date))})
    dfLast = pd.DataFrame({"Last": [last]})

    df = pd.DataFrame({'Last': calls.last, "Net": calls.net, 'Bib': calls.bib,
                       'Ask': calls.ask, 'Vol': calls.vol, 'IV': calls.IV,
                       "Delta": calls.delta, "Gamma": calls.gamma, "Int": calls.int})

    df1 = pd.DataFrame({'Last': spot.last, "Net": spot.net, 'Bib': spot.bib,
                        'Ask': spot.ask, 'Vol': spot.vol, 'IV': spot.IV,
                        "Delta": spot.delta, "Gamma": spot.gamma, "Int": spot.int})

    df2 = pd.DataFrame({"Strike": mid})
    writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', startcol=1, startrow=8)
    df1.to_excel(writer, sheet_name='Sheet1', startcol=15, startrow=8)
    df2.to_excel(writer, sheet_name='Sheet1', startcol=12, startrow=8)
    dfCall.to_excel(writer, sheet_name='Sheet1', startcol=1, startrow=6)
    dfSpot.to_excel(writer, sheet_name='Sheet1', startcol=15, startrow=6)
    dfDate.to_excel(writer, sheet_name='Sheet1', startcol=12, startrow=6)
    dfLast.to_excel(writer, sheet_name='Sheet1', startcol=12)


    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
