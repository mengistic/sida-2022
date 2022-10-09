

"""
1. Create a script named piapprox.py that let approximate
π by Gregory-Leibnitz series.
"""


N = 1000
pi = 0


for i in range(N):
    pi += 4*(-1)**i/(2*i+1)

print(pi)
