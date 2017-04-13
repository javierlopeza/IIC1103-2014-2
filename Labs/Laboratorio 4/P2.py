import sys
l1=int(sys.stdin.readline())
l2=int(sys.stdin.readline())
l3=int(sys.stdin.readline())
L=int(sys.stdin.readline())

def prob(l1, l2, L):
    if l1>L or (l2-l1)>L or (100-l2)>L:
        return 1
    else:
        return 0
 
def probabilidad(l1, l2, l3, L):
    c1=prob(l1,l2,L)
    c2=prob(l1,l3,L)
    c3=prob(l2,l3,L)
    g=(c1+c2+c3)/3
    return g
 
r=probabilidad(l1,l2,l3,L)
print(r)

