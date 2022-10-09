
"""
2. Create a script named pibyrandom.py that computes an approximation
of π by Monte-Carlo’s method, i.e. by choosing random points in the
unit square, and counting the proportion of them that lies in the unit
circle (distance from origin ⩽ 1). The user should be able to choose
how many random points will be generated :
"""


import random as rd

pi = 0
N = 10000
inside = 0

for i in range(N):
    x = rd.random()
    y = rd.random()
    d = x*x + y*y

    # count points inside circle
    if(d<=1): inside+=1

# area circle = 2*2 = 4
# area square = pi 

area_circle = inside
area_square = N
pi = 4*area_circle/area_square

print(pi)
    










