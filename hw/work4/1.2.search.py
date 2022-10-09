
import random as rd
import time

def sorted_array(n: int):
    a = [rd.randint(10, 20)]
    for i in range(n-1):
        last = a[i]
        a.append(rd.randint(last, last+5))
    return a





"""
In module search.py, write a function linear_search(a,e) that returns
True if element e in in the sorted array a and False if not. 
"""
def linear_search(a, e):
    L = len(a)
    for i in range(L):
        if (a[i] == e): return True

    return False





"""
Iterative Dichotomy
"""
def dichotomic_search(a, e):
    n = len(a)
    begin = 0
    end = n-1

    if(a[begin]>e or a[end]<e): return False

    while(n>1):
        mid = (begin+end)//2

        if   (a[mid]==e): return  True
        elif (a[mid]>e) : end   = mid-1
        else            : begin = mid+1

        n //= 2

    if a[begin]==e: return True
    return False


"""
Recursive Dichotomy
"""
def recursive_dicho(T, x, begin=0, end=-1):
    if end<0: end = len(T)-1
    if x<T[begin] or x>T[end]: return None

    m = (end+begin)//2 
    while(end>begin)  :
        if   (T[m]==x): return m
        elif (T[m]>x) : return recursive_dicho(T, x, begin, m-1)
        else          : return recursive_dicho(T, x, m+1, end)

    if(T[begin]==x): return m
    return None







"""
Testing
"""

N = 10
a = sorted_array(N)
e = rd.randint(10, 5*N)

N=10

for n in range(1000, 10000):
    total = 0
    for i in range(N):
        t0 = time.time()
        a = sorted_array(n)
        e = rd.randint(10, 5*n)
        dichotomic_search(a, e)
        t1 = time.time()

        total += t1-t0
        #print(total)

    print(n, total/N)

        
    

