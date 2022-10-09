def is_empty(T):
    if T==None or len(T)==0: return True
    return False

def is_sorted(T): return 
def root(T): return T[0]
def RST(T): return T[1]
def LST(T): return T[2]
def content(something): return something

def list_inorder(T): return 


######################################################
def max_BST1(T):
    """
    Iteratively
    O(h)
    """
    if is_empty(T): return None

    while(RST(T)!=None):
        T = RST(T)
    return content(root(T))

def max_BST2(T):
    """
    Recursively
    O(h)
    """
    if is_empty(T): return None
    if is_empty(RST(T)): return content(root(T))
    return max_BST(RST(T))

def max_BST(T): return max_BST2(T)

######################################################

def is_BST(T) -> bool: # O(n)
    return is_sorted(list_inorder(T))


def BST_search_bool(T, x) -> bool: #O(h)
    if is_empty(T): return False
    y = content(root(T))
    if x==y: return True
    if x<y: return BST_search(LST(T), x)
    return BST_search(RST(T), x)

def BST_search_tree(T, x): #tree
    if is_empty(T): return None
    y = content(root(T))
    if x==y: return T
    if x<y: return BST_search(LST(T), x)
    return BST_search(RST(T), x)

######################################################


def is_in(T, x) -> bool:
    if(is_empty(T)): return False

    y = content(root(T))
    if (x==y): return True
    if x<y: return is_in(LST(T), x)
    return is_in(RST(R), x)
        






######################################################
## insert 
## FIXME

def insert_BST(T:list , x:int ):
    new_node = [x, None,  None]

    if is_empty(T): return new_node

    L = LST(T)
    R = RST(T)

    y = content(root(T))
    if x<=y:
        if not(is_empty(L)):
            insert_BST(L, x)
        else: T[1]=new_node
    if x>y:
        if not(is_empty(R)):
            insert_BST(R, x)
        else: T[2]=new_node
    return T





## AVL Tree
## Balanced BST
