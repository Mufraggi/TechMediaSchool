import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("./data.csv")

fig = go.Figure()
fig.add_trace(go.Scatter(
                x=df['price'],
                y=df[' quanity demanded'],
                line_color='deepskyblue',
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df['price'],
                y=df[' quantity supplied'],
                line_color='dimgray',
                opacity=0.8))

fig.show()