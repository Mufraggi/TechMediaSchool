from  listing import Listing
from Manager import Manager

import pandas as pd



dataSet = pd.read_csv('./orders.csv')
manager = Manager(dataSet)
manager.createCsv()
#manager.findTransaction()

