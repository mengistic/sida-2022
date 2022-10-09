
def clamp(x: int, a: int, b:int):
    if x<=a: return a
    elif x>=b: return b
    else: return x


def f(n: int) -> int:
    return int(n/2) if n%2==0 else 3*n+1

def S(n: int):
    s_arr = [n]
    s = n
    while(s>1):
        s = f(s)
        s_arr.append(s)
    return s_arr


def ft(n: int): return len(S(n))

def ma(n: int): return max(S(n))

def hft(n: int) -> int:
    s_arr = S(n)
    L = len(s_arr)

    for i in range(L):
        s1 = s_arr[clamp(i, 0, L-1)]
        s2 = s_arr[clamp(i+1, 0, L-1)]

        if (s1>=n and s2<n): return i
        

def hft2() -> int:
    n = 3
    s_arr = [1, 4, 5, 7, 2, 1,  9, 3, 8, 10]
    L = len(s_arr)

    for i in range(L):
        s1 = s_arr[clamp(i, 0, L-1)]
        s2 = s_arr[clamp(i+1, 0, L-1)]

        if (s1>=n and s2<n): return i

print(hft2())

