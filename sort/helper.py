
import random as rd

def gen_array(n: int):
    a = []
    for i in range(n):
        a.append(rd.randint(1, n*n))
    return a

def is_sorted(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]: return False
    return True

