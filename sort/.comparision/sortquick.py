
import matplotlib.pyplot as plt
import csv
import random
import time

def gen_array(n):
    res = []
    for i in range(0, n):
        res.append(random.randint(0,n*n))
    return res

def is_sorted(T):
    for i in range(0, len(T)-1):
        if (T[i]>T[i+1]): return False
    return True

def choose_pivot_pos(begin, end):
    return random.randint(begin, end)

def partition_stable(T, begin, end, pos_pivot):
    """
    O(n) memory, not in place, stable
    """
    left = []
    right = []
    middle = [T[pos_pivot]]

    for i in range(begin,pos_pivot):
        if(T[i] < T[pos_pivot]): left.append(T[i])
        else: right.append(T[i])

    for i in range(pos_pivot+1, end+1):
        if(T[i] < T[pos_pivot]): left.append(T[i])
        else: right.append(T[i])

    T = left + middle + right
    return len(left)


def partition_inplace(a, begin, end, pos_pivot):
    """
    - Return the new position of pivot
    - O(1) memory, in place, not stable
    """
    pivot = a[pos_pivot]
    a[begin],a[pos_pivot] = a[pos_pivot],a[begin]

    i = begin+1
    j = end

    while(i<=j):
        if (a[i]<pivot): i += 1
        elif (a[j]>=pivot): j-=1
        else:
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1

    a[i-1],a[begin] = pivot,a[i-1]
    return i-1


def sort_quick(T, begin, end):
    if(end-begin+1>1):
        pos_pivot = choose_pivot_pos(begin, end)
        pos_pivot = partition_inplace(T, begin, end, pos_pivot)
        sort_quick(T, begin, pos_pivot-1)
        sort_quick(T, pos_pivot+1, end)

    return T


#T = [5,2,6,19,21,22,24,1,3,2]
#T = [6,6,10,2,4,5,8,21,1,2,6]

#T = [12, 35, 82, 95, 64, 73, 31, 20, 74, 15]
#pos= 5

#print("pos =", pos)
#print("pivot = ", T[pos])
#print(partition_inplace(T,0,len(T)-1, pos))
#

exp = 10
for n in range(1000,1001):
    total = 0
    for i in range(exp):
        T = gen_array(n)

        t1 = time.time()
        sort_quick(T, 0, n-1)
        t2 = time.time()
        total += t2-t1

    print(total/exp)
        
