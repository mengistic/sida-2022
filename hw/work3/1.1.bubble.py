
import random as rd

def random_array(n: int):
    a = []
    for i in range(n):
        a.append(rd.randint(0, 3*n))
    return a

print(random_array(6))

