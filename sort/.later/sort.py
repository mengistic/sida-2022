

"""
http://yunes.informatique.univ-paris-diderot.fr/en/jbys-webspace/
"""

import random as rd
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

def index_min(a, begin, end):
    m = begin

    for i in range(begin+1, end+1):
        if ( a[m]>a[i] ):
            m = i
    return m



def find_index(a, e):
    """
    Time Complexity: O(logn)
    """
    n = len(a)
    begin = 0
    end = n-1

    while(n>2):
        mid = (begin+end)//2
        if   (a[mid]==e): return  mid
        elif (a[mid]>e) : end   = mid
        else            : begin = mid
        n //= 2

    return mid

def sort_insertion_swap(a):
    """
    Time Complexity: O(n^2)
    """
    L = len(a)

    for i in range(1, L):
        j = i
        while(j>0 and a[j]<a[j-1]):
            temp = a[j]
            a[j]=a[j-1]
            a[j-1]=temp
            j -= 1

    return a


def sort_insertion_shift(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i-1
        while(j>=0 and a[j]>temp):
            a[j+1] = a[j]
            j-=1

        a[j+1] = temp

    return a
            

def binary_insert(a, x, begin, end):
    n = end-begin
    #begin = 0
    #end = n-1

    if(a[begin]>x): return 0
    elif(a[end]<x): return end+1

    while(n>1):
        mid = (begin+end)//2

        if   (a[mid]==x): return  mid+1
        elif (a[mid]>x) : end   = mid
        else            : begin = mid+1

        n //= 2

    if a[begin]>x: return begin
    return begin+1
    
#a = [7, 8, 9, 16, 18]
#T = [2,5,7,12, 15, 4]
#print(binary_insert(a, 13, 0, 4))

def sort_insertion_binary(a):
    for i in range(1, len(a)):
        temp = a[i]
        here = binary_insert(a,temp, 0,i-1)

        #print("a =", a[0:i])
        #print("a[i] =", temp)
        #print("here =", here)
        #print("```````````````````````")

        if here<i:
            for j in range(i, here, -1):
                a[j] = a[j-1]
            a[here] = temp

    return a

    
#T = gen_array(10)
#T = [16, 18, 7, 9, 8, 13]
#print(T)
#print("```````````````````````")


#ans = sort_insertion_binary(T)
#print(ans)
#print(is_sorted(ans))


        

#def sort_insertion_binary(a):
#    for i in range(1, len(a)):
#        temp = a[i]

#a = gen_array(5)
#print(a)
#print(sort_insertion_shift(a))
    

#import matplotlib.pyplot as plt
#import csv
##
##
#n = []
#selection_algo = []
#insertion_algo = []
#
#
#
#with open('doc/sort/data_time.txt', 'r') as data:
#    plots = csv.reader(data, delimiter=' ')
#    for row in plots:
#        n.append(float(row[0]))
#        selection_algo.append(float(row[1]))
#        insertion_algo.append(float(row[2]))
#
#
#plt.plot(n, selection_algo)
#plt.plot(n, insertion_algo)
#plt.show()




"""
lkjdasf
"""


def clamp(x, a,b):
    if x<a: return a
    elif x>b: return b
    else: return x

def merging(T, begin, end, pivot):
    res = []
    i,j = begin,pivot+1
    a,b=0,0

    while (i<=pivot and j<=end):
        if (T[i]<T[j]):
            res.append(T[i])
            i += 1
        else:
            res.append(T[j])
            j += 1

    while i<=pivot:
        res.append(T[i])
        i+=1
    while j<=end:
        res.append(T[j])
        j+=1

    if (end<len(T)-1):
        for k in range(end+1, len(T)):
            res.append(T[k])

    return res


#a = [3,10,14,15,  2,5,9,12,15, 20]
#print(a)
#print(merging(a, 0,len(a)-4, 3))

def sort_merge(a, begin, end):
    mid = (end+begin)//2

    if end-begin>1:
        sort_merge(a, begin, mid)
        sort_merge(a, mid+1, end)

    return merging(a, begin, end, mid)
    

#T = [3,5,10,12,16, 7, 10, 12, 20, 25, 11, 12, -1, 9, 10 ]
#print(T)
#print(merging(T, 0, 9, 4))
#print(sort_merge(T, 0, len(T)))
    


def merging(a, begin, end, pivot):
    i,j = begin, pivot+1

    while(i<=pivot and j<=end):
        if a[i]>a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            #a[i],a[j] = a[j],a[i]
            #j += 1
        else:
            i += 1

    return a


#a = [3,10,14, 2,5,9]
#print(a)
#print(merging(a,0, len(a)-1, 2))
            
def sort_insertion_swap(a):
    """
    Time Complexity: O(n^2)
    """
    L = len(a)

    for i in range(1, L):
        j = i
        while(j>0 and a[j]<a[j-1]):
            temp = a[j]
            a[j]=a[j-1]
            a[j-1]=temp
            j -= 1

    return a
        


def insertion_swap_step(a, step):
    L = len(a)

    for i in range(step, L):
        j = i
        while(j>0 and a[j]<a[j-step]):
            temp = a[j]
            a[j]=a[j-step]
            a[j-step]=temp
            j -= step

    return a

def sort_shell(a):
    n = len(a)
    step = 1
    while (3*step+1<n):
        step = 3*step + 1

    while step>=1:
        insertion_swap_step(a, step)
        step //= 3

    return a



#a = [2,6,3,10,12,11,9]
a = gen_array(100)
#print(insertion_swap_step(a, 4))
print(sort_shell(a))
print(is_sorted(a))
