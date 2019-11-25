#!/usr/bin/env python3

import pandas as pd

data = pd.read_csv("orders.csv")
matches = {}

def check_for_match(i, j):
    if data['pair'][i] == data['pair'][j] and i != j \
        and f'{i}' not in matches and f'{j}' not in matches:
        if data['action'][i] == ' BUY' and data['action'][j] == ' SELL' \
            and data['price'][i] >= data['price'][j]:
            matches[f"{i}"] = j
            matches[f"{j}"] = i
    if len(data) > i+1:
        check_for_match(i+1, j)
    elif len(data) > j+1:
        check_for_match(0, j+1)
    else:
        pass

check_for_match(0, 0)

data.insert(len(data), 'match', 'REJECTED')
for m in matches:
    data['match'][float(m)] = matches[m]

data.to_csv('result.csv', index=False, sep=',')
