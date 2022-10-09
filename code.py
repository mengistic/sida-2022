
from ctypes import string_at
import random

def radom_array(n):
    res  = []
    for i in range(n):
        res.append(random.randint(-60, 10))
    return res



def freeze_dac(T, begin, end) -> int:

    mid = (begin+end)//2

    if(end-begin==0):
        if T[begin]<0: return 1
        else: return 0

    else:
        L = freeze_dac(T, 0, mid)
        R = freeze_dac(T, mid+1, end)

        M = 0
        
        if(T[mid]<0):
            i=0
            while(mid-i>=0 and T[mid-i]<0):
                M += 1
                i += 1
                
            j=0
            while(mid+j<=end and T[mid+j]<0):
                M += 1
                j += 1
                
        return max(L, R, M-1)


def freeze(T):
    counter = 0
    length = 0

    assignment = 0

    for i in range(len(T)):
        if T[i]<0:
            counter += 1
            if (length<counter):
                length=counter
                assignment += 1
        else:
            counter = 0
        
    return assignment


def freeze_2(T):
    L = len(T)
    counter, length = 0, 0
    assignment = 0

    for i in range(L):
        if T[i]>=0: counter=0
        else:
            counter+=1 
            if( i>=L-1 or T[i+1]>=0  and length<counter):
                assignment += 1
                length=counter
        
    return assignment
    
    


#T = [2,-1, 5,9, -1,-2,-1]
#T = [2, -1,-2,-3, 4,5,9, 10, 11, -2,-10,-1,-2,-10,9, 4, -1,-1,-4,-5,10, 10]
#print("My previous: assignments =", freeze(T))
#print("Now:         assignments =", freeze_2(T))




def buystock_backend(T, begin, end):
    if (end-begin == 1): return (T[begin], T[begin])
    if (end-begin == 2):
        a = T[begin]
        b = T[begin+1]
        if (b>a): return (b, b)
        return (a, b)

    mid = (end+begin)//2
    (a,b) = buystock_backend(T, begin, mid)
    (c,d) = buystock_backend(T, mid, )
    return 





def syacuse(n: int):
    output_S = "S(" + str(n) + "): " + str(n) + " "
    ft = 0
    ma = n
    hft = 0

    S = n
    output_S = "S(" + str(n) + "): " + str(n) + " "
    check_hft = True

    while(S>1):
        if S%2==0: S //= 2
        else:
            S = 3*S + 1
            if (ma<S): ma = S

        output_S += str(S) + " "
        ft += 1

        if (S<n): check_hft = False
        if check_hft: hft += 1

    print(output_S)
    print(f"ft({n}) = {ft}")
    print(f"ma({n}) = {ma}")
    print(f"hft({n}) = {hft}\n")


syacuse(15)
syacuse(20)
