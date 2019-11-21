import json


with open('aa.json') as f:
    mylist = f.read().splitlines()

new = '['
for a in mylist:
    res = a.split(' ')
    new = new + "'" + (res[0]) + "'" + ","

new = new + ']'

print( new)