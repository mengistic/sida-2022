
import matplotlib.pyplot as plt
import csv
import random
import time 


def gen_array(n: int):
    a = []
    for i in range(n):
        a.append(rd.randint(1, n*n))
    return a

def is_sorted(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]: return False
    return True



def sort_insertion_swap(a):
    L = len(a)
    for i in range(1, L):
        j = i
        while(j>0 and a[j]<a[j-1]):
            a[j],a[j-1] = a[j-1],a[j]
            j -= 1
    return a
        


def insertion_swap_step(a, step):
    L = len(a)

    for i in range(step, L):
        j = i
        while(j>0 and a[j]<a[j-step]):
            a[j],a[j-step] = a[j-step],a[j]
            j -= step

    return a

def sort_shell(a):
    n = len(a)
    step = 1
    while (3*step+1<n): step = 3*step + 1

    while step>=1:
        insertion_swap_step(a, step)
        step //= 3

    return a



#a = [2,6,3,10,12,11,9]
#a = gen_array(10000)
#print(insertion_swap_step(a, 4))

#t1 = time.time()
#sort_insertion_swap(a)
#t2 = time.time()
#t = t2-t1
#print(is_sorted(a))
#print(t)


#exp = 10
#
#for n in range(900,1000):
#    total = 0
#    for i in range(exp):
#        a = gen_array(n)
#        t1 = time.time()
#        sort_insertion_swap(a)
#        t2 = time.time()
#
#        total += t2-t1
#
#    print(total/exp)


time_insert = []
time_shell = []
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


plt.plot(n, time_insert)
plt.plot(n, time_shell)
plt.show()
