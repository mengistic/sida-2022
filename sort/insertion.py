#import matplotlib.pyplot as plt
import random
#import time
#import csv

def gen_array(n):
    T = []
    for i in range(n):
        T.append(random.randint(1, n*n))
    return T

def is_sorted(T):
    for i in range(len(T)-1):
        if (T[i] > T[i+1]): return False
    return True


##
def sort_insertion_swap(a):
    L = len(a)
    for i in range(1, L):
        j = i
        while(j>0 and a[j]<a[j-1]):
            temp = a[j]
            a[j]=a[j-1]
            a[j-1]=temp
            j -= 1
    return a


## 
def sort_insertion_shift(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i-1
        while(j>=0 and a[j]>temp):
            a[j+1] = a[j]
            j-=1
        a[j+1] = temp
    return a
            

##
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
    
def sort_insertion_binary(a):
    for i in range(1, len(a)):
        temp = a[i]
        here = binary_insert(a,temp, 0,i-1)
        if here<i:
            for j in range(i, here, -1):
                a[j] = a[j-1]
            a[here] = temp
    return a


a = gen_array(100)
#sort_insertion_shift(a)
sort_insertion_binary(a)
print(is_sorted(a))
