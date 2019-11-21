import csv

import matplotlib.pyplot as plt


class data():
    def __init__(self, price, qD, qS):
        self.price = price
        self.quantityDemanded = qD
        self.quantitySupplied = qS



x = []
y = []
y2 = []
#price = []

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            x.append(row[0])
            y.append(row[1].replace(' ',''))
            y2.append(row[2].replace(' ',''))

#exit(0)



x.reverse()

x2 = x
plt.plot(x, y, color='g')

plt.plot(x2, y2, color='orange')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.legend()
plt.show()


#plt.plot(x, y)
#plt.plot(x, y2)

plt.show()
plt.close()

