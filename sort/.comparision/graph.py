import matplotlib.pyplot as plt
import csv
import random
import time 

time_insert = []
time_shell = []
time_quick = []
n = []


for i in range(100, 1000):
    n.append(i)

with open('data_insertion.dat', 'r') as data_insert:
    plots = csv.reader(data_insert, delimiter=' ')
    for row in plots:
        time_insert.append(float(row[0]))

with open('data_shell.dat', 'r') as data_shell:
    plots = csv.reader(data_shell, delimiter=' ')
    for row in plots:
        time_shell.append(float(row[0]))


with open('data_quick.dat', 'r') as data_quick:
    plots = csv.reader(data_quick, delimiter=' ')
    for row in plots:
        time_quick.append(float(row[0]))

plt.plot(n, time_insert)
plt.plot(n, time_shell)
plt.plot(n, time_quick)
plt.show()
