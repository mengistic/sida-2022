

import random as rd
import matplotlib as plt

def gen_sorted_array(n: int):
    a = [rd.randint(10, 20)]
    for i in range(n-1):
        last = a[i]
        a.append(rd.randint(last, last+5))
    return a





"""
In module search.py, write a function linear_search(a,e) that returns
True if element e in in the sorted array a and False if not. 
"""
def linear_search_call(a, e):
    call = 0
    L = len(a)

    for i in range(L):
        if (a[i] != e):
            call += 1
        else: return call

    return call




"""
Iterative Dichotomy
"""
def dicho_iter_call(a, e):
    call = 0

    n = len(a)
    begin = 0
    end = n-1

    if(a[begin]>e or a[end]<e): return call

    while(n>1):
        mid = (begin+end)//2

        if   (a[mid]==e): return  call
        elif (a[mid]>e) : end   = mid-1
        else            : begin = mid+1

        n //= 2
        call += 1

    #if a[begin]==e: return call
    return call-1




"""
Recursive Dichotomy
"""
def dicho_recur_call(T, x, begin=0, end=-1, call=0):
    if end<0: end = len(T)-1
    if x<T[begin] or x>T[end]: return call

    m = (end+begin)//2 
    while(end>begin)  :
        if   (T[m]==x): return call
        elif (T[m]>x) : return dicho_recur_call(T, x, begin, m-1, call+1)
        else          : return dicho_recur_call(T, x, m+1, end, call+1)


    return call









#a = [1, 3, 5, 10, 14, 15, 19, 21]
#a = gen_sorted_array(10)
#e = 2
#
#print(a)
#print(linear_search_call(a, e))
#print(dicho_iter_call(a, e))
#print(dicho_recur_call(a, e))

#for n in range(10, 10000):
#    a = gen_sorted_array(n)
#    e = rd.randint(1, 3*n)
#
#    linear    = linear_search_call(a, e)
#    iterative = dicho_iter_call(a, e)
#    recursive = dicho_recur_call(a, e)
#
#    print(n, linear, iterative, recursive)
