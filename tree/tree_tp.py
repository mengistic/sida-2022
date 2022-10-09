

T1 = None
T2 = [5, None, None]
T3 = [6,
      [1,
       [0, None, None],
       [3, None,
        [3, None, [5, [3, None, None], None]]]
       ],
      [7, None, [8, [7, None, None], None]]
]
T4 = [
    7,
    [0, None, [3, [1, None, [1, None, None]], [6, None, [6, None, None]]]],
    [9, [8, None, None], [9, None, None]]]

T5 = [
    5,
    [2, [0, None, None], [2, None, [3, [2, None, None], None]]],
    [9, [6, None, None], [9, None, [10, None, None]]]
]

forest = [T1, T2, T3, T4, T5]


######################################################

def is_empty(T): return (T==None)

def is_sorted(T): return 
def root(T):
    if T==None: return None
    return T[0]

def LST(T): return T[1]
def RST(T): return T[2]
def content(something):
    if something == None: return None
    return something



######################################################
def is_in(T, x) -> bool:   
    if(is_empty(T)): return False

    y = content(root(T))
    if (x==y): return True
    if x<y: return is_in(LST(T), x)
    return is_in(RST(T), x)



######################################################
def insert(T, x):   ## O(h)
    new_leaf = [x, None, None]

    if is_empty(T): return new_leaf

    y = content(root(T))
    R = RST(T)
    L = LST(T)

    if (x<=y):
        if not(is_empty(L)): insert(T[1], x)
        else: T[1]=new_leaf
    else:
        if not(is_empty(R)): insert(T[2], x)
        else: T[2]=new_leaf
        
    return T


######################################################

def height(T) -> int:
    if is_empty(T): return -1
    R = RST(T)
    L = LST(T)
    return 1+max(height(R),height(L))
    

def size(T) -> int:
    if is_empty(T): return 0

    R = RST(T)
    L = LST(T)
    return 1+size(R)+size(L)



#x = 2
#
#print(insert(T, x))

#x = int(input("insert x = "))
#
#T = None
#while(x!=-1):
#    T = insert(T, x)
#    print(T)
#    x = int(input("insert x = "))
    


######################################################
######################################################

def min_node(T):
    if is_empty(T): return 

    L = LST(T)
    if is_empty(L): return root(T)
    return min_node(L)


def max_node(T):
    if is_empty(T): return 
    R = RST(T)
    if is_empty(R): return root(T)
    return max_node(R)

def extract(T, x):
    if(is_empty(T)): return None

    y = content(root(T))
    if (x==y): return T
    if x<y: return extract(LST(T), x)
    return extract(RST(T), x)


def delete_max(T):
    if is_empty(T): return None

    MAX = 0
    L = LST(T)
    ROOT = content(root(T))

    if is_empty(R): return ROOT


    return MAX



######################################################


def BST_minimum(T):
    if is_empty(T): return None

    ROOT = T[0]
    LEFT = T[1]
    RIGHT = T[2]

    if is_empty(LEFT): return T
    return BST_minimum(LEFT)



def BST_delete(T, x):  ## O(h)
    if is_empty(T): return T

    ROOT  = T[0]
    LEFT  = T[1]
    RIGHT = T[2]

    if (x<ROOT): T[1] = BST_delete(LEFT, x)
    if (x>ROOT): T[2] = BST_delete(RIGHT, x)
    else:
        if is_empty(LEFT) and is_empty(RIGHT): return None
        elif is_empty(LEFT):
            T[0] = RIGHT[0] #content(root(RIGHT))
            T[1] = RIGHT[1] #RIGHT[1]
            T[2] = RIGHT[2] #RIGHT[2]
        elif is_empty(RIGHT):
            T[0] = LEFT[0] #content(root(LEFT))
            T[1] = LEFT[1] #LEFT[1]
            T[2] = LEFT[2] #LEFT[2]
        else:
            t_min = BST_minimum(T[2])
            T[0] = t_min[0]
            t_min = BST_delete(t_min, T[0])
    return T
            

#print(T3)
#print(BST_delete(T3, 3))



T = [3, None, [5, 3, None]]
TT = [1, [0,None,None], T]

TTT = [5, [3,None,None], None]

T0 = [3,None,None]
T1 = [5, T0, None]
T2 = [3, None, T1]
T3 = [1, [0,None,None], T2]

T4=[7, None, [8,[7,None,None], None]]

T = [6, T3, T4]

print(T4)
print(BST_delete(T4, 3))

print(T4)
