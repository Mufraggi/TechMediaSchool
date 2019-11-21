import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


print("Please enter a product")
product = str(input())
print("Please enter the maximum quantity ")
quantity = int(input())

happines = []
nbProduct = []

for number in range(1, quantity + 1):
    print("For {} {} what added happiness do you get? ".format(number, product))
    nbProduct.append(number)
    happines.append(int(input()))

print(nbProduct)
print(happines)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=nbProduct,
    y=happines,
    marker=dict(color="crimson", size=12),
    mode="markers"
))
fig.show()