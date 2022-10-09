
import matplotlib.pyplot as plt
import numpy as np
import csv


x = []
y = []


with open('data1.txt', 'r') as data:
    plots = csv.reader(data, delimiter=' ')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[2]))

z = np.log2(x)

plt.plot(x, y, 'bo')
plt.plot(x, z)
plt.show()
