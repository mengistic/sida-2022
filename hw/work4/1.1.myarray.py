
import random as rd

def sorted_array(n: int):
    a = [rd.randint(10, 20)]
    for i in range(n-1):
        last = a[i]
        a.append(rd.randint(last, last+5))
    return a

print(sorted_array(6))
