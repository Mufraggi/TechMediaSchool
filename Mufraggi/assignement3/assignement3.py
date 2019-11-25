import plotly.graph_objects as go
import pandas as pd
import plotly.express as px




gdp = pd.read_csv("world_bank_gdp.csv", sep=',', skiprows=[0,1,2,3])
tarrif = pd.read_csv('world_bank_tariff.csv', sep=',', skiprows=[0,1,2,3])

gdp = gdp[gdp["2017"].notnull()]
tarrif = tarrif[tarrif["2017"].notnull()]
ultimeCsv = pd.merge(gdp, tarrif ,on=['Country Name','Country Code']).sample(10)
#print(ultimeCsv)

fig = px.scatter(ultimeCsv, x="2017_x", y="2017_y", color="Country Name" )

fig.show()

