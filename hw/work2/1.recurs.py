
# 1 
from array import array
from ctypes import string_at


def fact_iterative(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def fact_rec(n):
    if n>0: return n*fact_rec(n-1)
    else: return 1




# 2

def to_binary(n: int) -> int:
    if (n>0):
        return to_binary(n//2)*10 + n%2
    return 0

def to_binary_string(n: int) -> str:
    if (n>0):
        return to_binary_string(n//2) + str(n%2)
    return ""


list = []
def to_bin_list(n: int):
    if (n>0):
        list.insert(0, n%2)
        to_bin_list(n//2)


print(to_binary_string(37))
print(to_binary(37))
to_bin_list(37)
print(list)


#print(to_binary(37))

# 3
def fibonacci(n: int) -> int:
    if n>1: return fibonacci(n-1)+fibonacci(n-2)
    else: return 1


# 4
def gcd(a:int , b:int):
    if b==0: return a
    else: return gcd(b, a%b)


# 5: Pascal
def pascal(n):
    result = []
    p = [1]

    if (n==0):
        print(p)
        return p
    elif (n==1):
        print([1])
        print([1,1])
        return [1,1]
    else:
        q = pascal(n-1)
        for i in range(1, len(q)):
            new = q[i-1]+q[i]
            p.append(new)
        p.append(1)
        print(" "*(5-n),p)
        print(p)

    return p





# 6
