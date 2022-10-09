import matplotlib.pyplot as plt
import random
import time
import csv

def gen_array(n):
    T = []
    for i in range(n):
        T.append(random.randint(1, n*n))
    return T

def is_sorted(T):
    for i in range(len(T)-1):
        if (T[i] > T[i+1]): return False
    return True



def sort_selection(T):
    L = len(T)

    for i in range(0, L-1):
        m = i+1
        for j in range(i+1, L):
            if (T[m]>T[j]): m=j

        if (T[i]>T[m]): T[i],T[m] = T[m],T[i]

    return T


# time complexity
#exp = 10
#for n in range(1400, 1500):
#    total = 0
#    for i in range(exp):
#        T = gen_array(n)
#        t1 = time.time()
#        sort_selection(T)
#        t2 = time.time()
#        total += t2-t1
#    print(total/exp)


graph_time = []
n = []

for i in range(100, 1500):
    n.append(i)

with open('data_time.dat', 'r') as data_time:
    plots = csv.reader(data_time, delimiter=' ')
    for row in plots:
        graph_time.append(float(row[0]))


plt.plot(n, graph_time)
plt.show()
