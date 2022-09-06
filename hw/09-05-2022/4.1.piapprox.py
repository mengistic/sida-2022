

"""
1. Create a script named piapprox.py that let approximate
π by Gregory-Leibnitz series.
"""


def minus_one_to_n(n):
    #return n%2==0 ? 1:-1
    if n%2==0: return 1
    else: return -1

N = 1000
pi = 0


for i in range(N):
    pi += 4*minus_one_to_n(i)/(2*i+1)

print(pi)
